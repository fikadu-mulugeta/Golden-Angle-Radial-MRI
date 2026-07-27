"""
phantom.py

Functions for generating digital MRI phantoms.

"""

import numpy as np
from skimage.data import shepp_logan_phantom
from skimage.transform import resize


def generate_shepp_logan(size: int = 256) -> np.ndarray:
    """
    Generate a resized Modified Shepp-Logan phantom.

    Parameters
    ----------
    size : int, optional
        Output image size (size × size). Default is 256.

    Returns
    -------
    np.ndarray
        Phantom image normalized between 0 and 1.
    """

    if size <= 0:
        raise ValueError("size must be a positive integer.")
    if not isinstance(size, int):
        raise TypeError("size must be an integer.")

    phantom = shepp_logan_phantom()

    phantom = resize(
        phantom,
        (size, size),
        anti_aliasing=True,
        preserve_range=True,
    )

    return phantom.astype(np.float32)


def generate_circle(
    size: int = 256,
    radius: int = 70,
    center: tuple[int, int] | None = None
) -> np.ndarray:
    """
    Generate a binary circular phantom.

    Parameters
    ----------
    size : int
        Image size.

    radius : int
        Circle radius.

    center : tuple[int, int] | None
        Circle center. If None, uses the image center.

    Returns
    -------
    np.ndarray
        Binary circle phantom.
    """

    if size <= 0:
        raise ValueError("size must be positive.")

    if radius <= 0:
        raise ValueError("radius must be positive.")

    if center is None:
        center = (size // 2, size // 2)

    cx, cy = center
    cx, cy = center

    if not (0 <= cx < size and 0 <= cy < size):
        raise ValueError(
        "center must lie inside the image."
    )

    y, x = np.ogrid[:size, :size]

    distance_squared = (x - cx) ** 2 + (y - cy) ** 2

    phantom = np.zeros((size, size), dtype=np.float32)

    phantom[distance_squared <= radius ** 2] = 1.0

    return phantom


def generate_rectangle(
    size: int = 256,
    width: int = 120,
    height: int = 80
) -> np.ndarray:
    """
    Generate a centered binary rectangle phantom.

    Parameters
    ----------
    size : int
        Image size.

    width : int
        Rectangle width.

    height : int
        Rectangle height.

    Returns
    -------
    np.ndarray
        Binary rectangle phantom.
    """

    if size <= 0:
        raise ValueError("size must be positive.")

    phantom = np.zeros((size, size), dtype=np.float32)

    if width <= 0 or width > size:
        raise ValueError(
        "width must satisfy 0 < width <= size."
    )

    if height <= 0 or height > size:
        raise ValueError(
        "height must satisfy 0 < height <= size."
    )

    x0 = (size - width) // 2
    x1 = x0 + width

    y0 = (size - height) // 2
    y1 = y0 + height

    phantom[y0:y1, x0:x1] = 1.0

    return phantom


def generate_multiple_circles(
    size: int = 256
) -> np.ndarray:
    """
    Generate a phantom containing multiple circles of
    different sizes and intensities.

    Parameters
    ----------
    size : int

    Returns
    -------
    np.ndarray
        Multi-circle phantom.
    """

    if size <= 0:
        raise ValueError("size must be positive.")

    phantom = np.zeros((size, size), dtype=np.float32)

    y, x = np.ogrid[:size, :size]

    circles = [
        ((size * 0.30, size * 0.30), size * 0.12, 1.0),
        ((size * 0.70, size * 0.30), size * 0.08, 0.8),
        ((size * 0.50, size * 0.60), size * 0.15, 0.6),
        ((size * 0.35, size * 0.75), size * 0.06, 0.9),
        ((size * 0.75, size * 0.75), size * 0.10, 0.5),
    ]

    for center, radius, intensity in circles:

        cx, cy = center

        mask = (x - cx) ** 2 + (y - cy) ** 2 <= radius ** 2

        phantom[mask] = intensity

    return phantom