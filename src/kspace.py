"""
kspace.py

Utilities for visualizing and manipulating MRI k-space.

"""

import numpy as np


def log_magnitude(kspace: np.ndarray) -> np.ndarray:
    """
    Compute the log-scaled magnitude of k-space.

    This compresses the large dynamic range of k-space,
    making both low- and high-frequency components visible.

    Parameters
    ----------
    kspace : np.ndarray
        Complex-valued k-space.

    Returns
    -------
    np.ndarray
        Log-scaled magnitude image.
    """

    return np.log1p(np.abs(kspace))


def center_crop(
    kspace: np.ndarray,
    fraction: float = 0.25
) -> np.ndarray:
    """
    Keep only the central portion of k-space
    (low spatial frequencies).

    Parameters
    ----------
    kspace : np.ndarray
        Complex-valued k-space.

    fraction : float
        Fraction of k-space to preserve.

    Returns
    -------
    np.ndarray
        Cropped k-space.
    """

    rows, cols = kspace.shape

    r = int(rows * fraction / 2)
    c = int(cols * fraction / 2)

    center_row = rows // 2
    center_col = cols // 2

    cropped = np.zeros_like(kspace)

    cropped[
        center_row-r:center_row+r,
        center_col-c:center_col+c
    ] = kspace[
        center_row-r:center_row+r,
        center_col-c:center_col+c
    ]

    return cropped


def remove_center(
    kspace: np.ndarray,
    fraction: float = 0.25
) -> np.ndarray:
    """
    Remove the central portion of k-space
    (low spatial frequencies).

    Parameters
    ----------
    kspace : np.ndarray
        Complex-valued k-space.

    fraction : float
        Fraction of the center to remove.

    Returns
    -------
    np.ndarray
        Modified k-space.
    """

    modified = kspace.copy()

    rows, cols = modified.shape

    r = int(rows * fraction / 2)
    c = int(cols * fraction / 2)

    center_row = rows // 2
    center_col = cols // 2

    modified[
        center_row-r:center_row+r,
        center_col-c:center_col+c
    ] = 0

    return modified


def remove_edges(
    kspace: np.ndarray,
    fraction: float = 0.25
) -> np.ndarray:
    """
    Remove the edges of k-space
    (high spatial frequencies).

    Parameters
    ----------
    kspace : np.ndarray
        Complex-valued k-space.

    fraction : float
        Fraction of the center to preserve.

    Returns
    -------
    np.ndarray
        Modified k-space containing only
        low spatial frequencies.
    """

    return center_crop(kspace, fraction)


def energy(kspace: np.ndarray) -> float:
    """
    Compute the total energy of k-space.

    Parameters
    ----------
    kspace : np.ndarray
        Complex-valued k-space.

    Returns
    -------
    float
        Total k-space energy.
    """

    return float(np.sum(np.abs(kspace) ** 2))