"""
image_utils.py

General-purpose image processing, visualization, and analysis
utilities used throughout the MRI acquisition and reconstruction
experiments.

"""

import numpy as np
import matplotlib.pyplot as plt

from skimage.transform import resize


def normalize_image(image: np.ndarray) -> np.ndarray:
    """
    Normalize an image to the range [0, 1].

    Parameters
    ----------
    image : np.ndarray
        Input image.

    Returns
    -------
    np.ndarray
        Normalized image.
    """

    image = image.astype(np.float32)

    min_val = np.min(image)
    max_val = np.max(image)

    if max_val == min_val:
        return np.zeros_like(image)

    return (image - min_val) / (max_val - min_val)


def resize_image(
    image: np.ndarray,
    size: int
) -> np.ndarray:
    """
    Resize an image to (size × size).

    Parameters
    ----------
    image : np.ndarray
        Input image.

    size : int
        Desired image size.

    Returns
    -------
    np.ndarray
        Resized image.
    """

    if size <= 0:
        raise ValueError("size must be positive.")

    resized = resize(
        image,
        (size, size),
        anti_aliasing=True,
        preserve_range=True
    )

    return resized.astype(np.float32)


def display_image(
    image: np.ndarray,
    title: str = "Image",
    cmap: str = "gray",
    figsize: tuple[int, int] = (6, 6)
) -> None:
    """
    Display an image using Matplotlib.

    Parameters
    ----------
    image : np.ndarray
        Image to display.

    title : str
        Figure title.

    cmap : str
        Matplotlib colormap.

    figsize : tuple[int, int]
        Figure size.
    """

    plt.figure(figsize=figsize)

    plt.imshow(image, cmap=cmap)

    plt.title(title)

    plt.axis("off")

    plt.show()


def image_statistics(
    image: np.ndarray
) -> dict:
    """
    Compute basic image statistics.

    Parameters
    ----------
    image : np.ndarray
        Input image.

    Returns
    -------
    dict
        Dictionary containing image statistics.
    """

    stats = {
        "Shape": image.shape,
        "Data Type": image.dtype,
        "Minimum": float(np.min(image)),
        "Maximum": float(np.max(image)),
        "Mean": float(np.mean(image)),
        "Standard Deviation": float(np.std(image)),
    }

    return stats


def compare_images(
    image1: np.ndarray,
    image2: np.ndarray,
    title1: str = "Image 1",
    title2: str = "Image 2"
) -> None:
    """
    Display two images side-by-side.

    Parameters
    ----------
    image1 : np.ndarray
        First image.

    image2 : np.ndarray
        Second image.

    title1 : str
        Title of first image.

    title2 : str
        Title of second image.
    """

    fig, axes = plt.subplots(1, 2, figsize=(10, 5))

    axes[0].imshow(image1, cmap="gray")
    axes[0].set_title(title1)
    axes[0].axis("off")

    axes[1].imshow(image2, cmap="gray")
    axes[1].set_title(title2)
    axes[1].axis("off")

    plt.tight_layout()

    plt.show()