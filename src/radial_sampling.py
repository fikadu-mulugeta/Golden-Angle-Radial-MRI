"""
radial_sampling.py

Utility functions for simulating radial MRI k-space acquisition.
"""

from .fft import ifft2c
import numpy as np


def generate_radial_angles(num_spokes: int) -> np.ndarray:
    """
    Generate uniformly spaced radial projection angles.

    Parameters
    ----------
    num_spokes : int
        Number of radial spokes.

    Returns
    -------
    np.ndarray
        Projection angles in radians.
    """
    if num_spokes <= 0:
      raise ValueError("num_spokes must be greater than zero.")

    return np.linspace(
        start=0.0,
        stop=np.pi,
        num=num_spokes,
        endpoint=False,
        dtype=np.float32,
    )

def generate_trajectory(
    angles: np.ndarray,
    num_samples: int,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate Cartesian coordinates for an arbitrary MRI trajectory.

    Parameters
    ----------
    angles : np.ndarray
        Projection angles in radians.

    num_samples : int
        Number of sampling points along each spoke.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        kx and ky trajectory coordinates.
    """

    if angles.ndim != 1:
        raise ValueError("angles must be a 1D array.")

    if num_samples <= 1:
        raise ValueError("num_samples must be greater than one.")

    radius = np.linspace(
        start=-1.0,
        stop=1.0,
        num=num_samples,
        dtype=np.float32,
    )

    num_spokes = len(angles)

    kx = np.zeros(
        (num_spokes, num_samples),
        dtype=np.float32,
    )

    ky = np.zeros(
        (num_spokes, num_samples),
        dtype=np.float32,
    )

    # Compute Cartesian coordinates.
    for spoke_index, theta in enumerate(angles):

        kx[spoke_index] = radius * np.cos(theta)
        ky[spoke_index] = radius * np.sin(theta)

    return kx, ky

def create_mask_from_trajectory(
    shape: tuple[int, int],
    kx: np.ndarray,
    ky: np.ndarray,
) -> np.ndarray:
    """
    Create a binary sampling mask from trajectory coordinates.

    Parameters
    ----------
    shape : tuple[int, int]
        Shape of the k-space.

    kx : np.ndarray
        k-space x coordinates.

    ky : np.ndarray
        k-space y coordinates.

    Returns
    -------
    np.ndarray
        Binary sampling mask.
    """

    if len(shape) != 2:
        raise ValueError("shape must contain two dimensions.")

    rows, cols = shape

    mask = np.zeros(
        shape,
        dtype=np.float32,
    )

    x = ((kx + 1) / 2 * (cols - 1)).astype(int)

    y = ((ky + 1) / 2 * (rows - 1)).astype(int)

    valid = (
        (x >= 0)
        & (x < cols)
        & (y >= 0)
        & (y < rows)
    )

    mask[y[valid], x[valid]] = 1

    return mask

def generate_radial_trajectory(
    num_spokes: int,
    num_samples: int,
) -> tuple[np.ndarray, np.ndarray]:
    """
    Generate Cartesian coordinates for a radial MRI trajectory.

    Parameters
    ----------
    num_spokes : int
        Number of radial spokes.

    num_samples : int
        Number of sampling points along each spoke.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        kx and ky trajectory coordinates.
    """
    if num_spokes <= 0:
      raise ValueError("num_spokes must be greater than zero.")

    angles = generate_radial_angles(num_spokes)

    return generate_trajectory(
      angles=angles,
      num_samples=num_samples,
)

def create_radial_mask(
    shape: tuple[int, int],
    num_spokes: int,
) -> np.ndarray:
    """
    Create a binary radial sampling mask.

    Parameters
    ----------
    shape : tuple[int, int]
        Shape of the k-space.

    num_spokes : int
        Number of radial spokes.

    Returns
    -------
    np.ndarray
        Binary sampling mask.
    """
    if len(shape) != 2:
      raise ValueError("shape must contain two dimensions.")

    if num_spokes <= 0:
      raise ValueError("num_spokes must be greater than zero.")

    kx, ky = generate_radial_trajectory(
      num_spokes=num_spokes,
      num_samples=max(shape),
    )

    return create_mask_from_trajectory(
      shape=shape,
      kx=kx,
      ky=ky,
    )

def apply_radial_sampling(
    kspace: np.ndarray,
    mask: np.ndarray,
) -> np.ndarray:
    """
    Apply a radial sampling mask to k-space.

    Parameters
    ----------
    kspace : np.ndarray
        Full Cartesian k-space.

    mask : np.ndarray
        Binary radial sampling mask.

    Returns
    -------
    np.ndarray
        Radially sampled k-space.
    """

    if kspace.shape != mask.shape:
      raise ValueError(
        "kspace and mask must have the same shape."
    )

    return kspace * mask

def sampling_percentage(mask: np.ndarray) -> float:
    """
    Compute the percentage of sampled k-space.

    Parameters
    ----------
    mask : np.ndarray
        Binary sampling mask.

    Returns
    -------
    float
        Sampling percentage.
    """

    if mask.ndim != 2:
      raise ValueError("mask must be a 2D array.")

    sampled_points = np.count_nonzero(mask)

    total_points = mask.size

    return 100.0 * sampled_points / total_points


def reconstruct_radial_image(
    sampled_kspace: np.ndarray,
) -> np.ndarray:
    """
    Reconstruct an image from radially sampled k-space.

    Parameters
    ----------
    sampled_kspace : np.ndarray
        Radially sampled k-space.

    Returns
    -------
    np.ndarray
        Reconstructed magnitude image.
    """

    if sampled_kspace.ndim != 2:
      raise ValueError(
        "sampled_kspace must be a 2D array."
    )

    return np.abs(ifft2c(sampled_kspace))