"""
golden_angle.py

Utility functions for generating golden-angle radial
MRI sampling trajectories and sampling masks.
"""



import numpy as np
from .radial_sampling import (
    generate_trajectory,
    create_mask_from_trajectory,
)


def generate_golden_angle() -> float:
    """
    Return the MRI golden angle in radians.
    """

    return np.deg2rad(111.246)


def generate_golden_angles(
    num_spokes: int,
) -> np.ndarray:
    """
    Generate golden-angle projection angles.
    """

    if num_spokes <= 0:
        raise ValueError(
            "num_spokes must be greater than zero."
        )

    golden = generate_golden_angle()

    return np.mod(
        np.arange(num_spokes) * golden,
        np.pi,
    ).astype(np.float32)


def generate_golden_trajectory(
    num_spokes: int,
    num_samples: int,
):
    """
    Generate a golden-angle radial trajectory.
    """

    angles = generate_golden_angles(
        num_spokes,
    )

    return generate_trajectory(
        angles,
        num_samples,
    )


def create_golden_mask(
    shape,
    num_spokes,
):
    """
    Create a golden-angle sampling mask.
    """

    kx, ky = generate_golden_trajectory(
        num_spokes,
        max(shape),
    )

    return create_mask_from_trajectory(
        shape,
        kx,
        ky,
    )



