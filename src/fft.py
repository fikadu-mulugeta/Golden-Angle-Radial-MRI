"""
fft.py

Centered Fourier Transform utilities for MRI reconstruction.
"""

import numpy as np


def fft2c(image: np.ndarray) -> np.ndarray:
    """
    Compute the centered 2D Fourier Transform.

    Parameters
    ----------
    image : np.ndarray
        Input image in image space.

    Returns
    -------
    np.ndarray
        Complex-valued centered k-space.
    """

    return np.fft.fftshift(
        np.fft.fft2(
            np.fft.ifftshift(image)
        )
    )


def ifft2c(kspace: np.ndarray) -> np.ndarray:
    """
    Compute the centered inverse 2D Fourier Transform.

    Parameters
    ----------
    kspace : np.ndarray
        Complex-valued centered k-space.

    Returns
    -------
    np.ndarray
        Complex-valued reconstructed image.
    """

    return np.fft.fftshift(
        np.fft.ifft2(
            np.fft.ifftshift(kspace)
        )
    )


def magnitude(data: np.ndarray) -> np.ndarray:
    """
    Compute the magnitude of complex-valued data.

    Parameters
    ----------
    data : np.ndarray
        Complex-valued array.

    Returns
    -------
    np.ndarray
        Magnitude image.
    """

    return np.abs(data)


def phase(data: np.ndarray) -> np.ndarray:
    """
    Compute the phase of complex-valued data.

    Parameters
    ----------
    data : np.ndarray
        Complex-valued array.

    Returns
    -------
    np.ndarray
        Phase image in radians.
    """

    return np.angle(data)