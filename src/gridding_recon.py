"""
gridding.py

Utilities for sampling, density compensation,
gridding, and image reconstruction for
non-Cartesian MRI trajectories.
"""

import numpy as np
from .fft import ifft2c

def _trajectory_to_pixel_indices(
    kx: np.ndarray,
    ky: np.ndarray,
    shape: tuple[int, int],
) -> tuple[np.ndarray, np.ndarray]:
    """
    Convert normalized trajectory coordinates into
    Cartesian pixel indices.

    Parameters
    ----------
    kx : np.ndarray
        Normalized x coordinates in [-1, 1].

    ky : np.ndarray
        Normalized y coordinates in [-1, 1].

    shape : tuple[int, int]
        Cartesian grid shape.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        Integer x and y pixel indices.
    """

    rows, cols = shape

    x = np.round(
        (kx + 1) / 2 * (cols - 1)
    ).astype(np.int32)

    y = np.round(
        (ky + 1) / 2 * (rows - 1)
    ).astype(np.int32)

    return x, y



def sample_kspace(
    kspace: np.ndarray,
    kx: np.ndarray,
    ky: np.ndarray,
) -> np.ndarray:
    """
    Sample Cartesian k-space along a radial trajectory.

    Parameters
    ----------
    kspace : np.ndarray
        Cartesian k-space.

    kx, ky : np.ndarray
        Normalized trajectory coordinates.

    Returns
    -------
    np.ndarray
        Complex-valued trajectory samples.
    """

    if kspace.ndim != 2:
        raise ValueError("kspace must be 2D.")

    if kx.shape != ky.shape:
        raise ValueError(
            "kx and ky must have identical shapes."
        )

    x, y = _trajectory_to_pixel_indices(
        kx,
        ky,
        kspace.shape,
    )

    samples = np.zeros(
        kx.shape,
        dtype=kspace.dtype,
    )

    valid = (
        (x >= 0)
        & (x < kspace.shape[1])
        & (y >= 0)
        & (y < kspace.shape[0])
    )

    samples[valid] = kspace[
        y[valid],
        x[valid],
    ]

    return samples


def compute_density_map(
    kx: np.ndarray,
    ky: np.ndarray,
    shape: tuple[int, int],
) -> np.ndarray:
    """
    Count how many trajectory samples fall inside each
    Cartesian pixel.

    Returns
    -------
    np.ndarray
        Sampling density map.
    """

    x, y = _trajectory_to_pixel_indices(
        kx,
        ky,
        shape,
    )

    density = np.zeros(
        shape,
        dtype=np.float32,
    )

    valid = (
        (x >= 0)
        & (x < shape[1])
        & (y >= 0)
        & (y < shape[0])
    )

    for xi, yi in zip(x[valid], y[valid]):
        density[yi, xi] += 1

    return density



def simple_dcf(
    kx: np.ndarray,
    ky: np.ndarray,
) -> np.ndarray:
    """
    Compute a simple radial Density Compensation Function.

    The weight assigned to each sample is proportional
    to its distance from the center of k-space.
    This simplified density compensation function is intended for 
    computational investigations. It is not equivalent to iterative 
    or analytically derived density compensation 
    methods used in clinical MRI reconstruction.

    Returns
    -------
    np.ndarray
        Density compensation weights.
    """

    radius = np.sqrt(
        kx**2 + ky**2
    )

    radius /= radius.max()

    return radius.astype(np.float32)



def apply_dcf(
    samples: np.ndarray,
    weights: np.ndarray,
) -> np.ndarray:
    """
    Apply density compensation.

    Parameters
    ----------
    samples : np.ndarray
        Complex-valued trajectory samples.

    weights : np.ndarray
        Density compensation weights.

    Returns
    -------
    np.ndarray
        Weighted trajectory samples.
    """

    if samples.shape != weights.shape:
        raise ValueError(
            "samples and weights must have identical shapes."
        )

    return samples * weights



def grid_nearest(
    samples: np.ndarray,
    kx: np.ndarray,
    ky: np.ndarray,
    shape: tuple[int, int],
) -> np.ndarray:
    """
    Grid trajectory samples onto a Cartesian grid using
    nearest-neighbor interpolation.
    """

    x, y = _trajectory_to_pixel_indices(
        kx,
        ky,
        shape,
    )

    grid = np.zeros(
        shape,
        dtype=np.complex64,
    )

    counts = np.zeros(
        shape,
        dtype=np.float32,
    )

    valid = (
        (x >= 0)
        & (x < shape[1])
        & (y >= 0)
        & (y < shape[0])
    )

    for xi, yi, value in zip(
        x[valid],
        y[valid],
        samples[valid],
    ):

        grid[yi, xi] += value
        counts[yi, xi] += 1

    mask = counts > 0

    grid[mask] /= counts[mask]

    return grid



def reconstruct_image(
    kspace: np.ndarray,
) -> np.ndarray:
    """
    Reconstruct an image from gridded Cartesian k-space.

    Parameters
    ----------
    kspace : np.ndarray
        Gridded Cartesian k-space.

    Returns
    -------
    np.ndarray
        Magnitude image.
    """

    return np.abs(
        ifft2c(kspace)
    )



