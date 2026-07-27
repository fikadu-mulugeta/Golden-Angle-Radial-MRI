"""
cartesian_sampling.py

Utilities for simulating Cartesian k-space sampling
and undersampling in MRI.
"""

import numpy as np


def create_full_mask(shape: tuple) -> np.ndarray:
    """
    Create a fully sampled Cartesian mask.

    Parameters
    ----------
    shape : tuple
        Shape of the k-space.

    Returns
    -------
    np.ndarray
        Mask containing only ones.
    """

    return np.ones(shape, dtype=np.float32)


def create_cartesian_mask(
    shape: tuple,
    acceleration: int = 2
) -> np.ndarray:
    """
    Create a uniformly undersampled Cartesian mask.

    Every 'acceleration'-th phase-encoding line is acquired.
    Rows are assumed to represent the phase-encoding direction.

    Parameters
    ----------
    shape : tuple
        Shape of the k-space.

    acceleration : int, default=2
        Sampling acceleration factor.

    Returns
    -------
    np.ndarray
        Cartesian sampling mask.
    """

    if acceleration < 1:
        raise ValueError("Acceleration factor must be >= 1.")

    mask = np.zeros(shape, dtype=np.float32)

    mask[::acceleration, :] = 1

    return mask


def apply_sampling_mask(
    kspace: np.ndarray,
    mask: np.ndarray
) -> np.ndarray:
    """
    Apply a Cartesian sampling mask.

    Parameters
    ----------
    kspace : np.ndarray
        Full k-space.

    mask : np.ndarray
        Cartesian sampling mask.

    Returns
    -------
    np.ndarray
        Sampled k-space.
    """

    return kspace * mask


def sampling_percentage(mask: np.ndarray) -> float:
    """
    Compute the percentage of acquired samples.

    Parameters
    ----------
    mask : np.ndarray
        Sampling mask.

    Returns
    -------
    float
        Sampling percentage.
    """

    return 100 * np.mean(mask)


def acceleration_factor(mask: np.ndarray) -> float:
    """
    Estimate the acceleration factor.

    Parameters
    ----------
    mask : np.ndarray
        Sampling mask.

    Returns
    -------
    float
        Acceleration factor.
    """

    sampled = np.mean(mask)

    if sampled == 0:
        raise ValueError("Sampling mask contains no acquired samples.")

    return 1 / sampled