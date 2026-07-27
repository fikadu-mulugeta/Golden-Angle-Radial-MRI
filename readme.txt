# MRI Acquisition and Image Reconstruction: A Computational Investigation

A computational investigation into the fundamental principles of Magnetic Resonance Imaging (MRI), including image formation, Fourier reconstruction, k-space sampling, accelerated MRI acquisition, radial imaging, golden-angle sampling, and simplified non-Cartesian image reconstruction.

This repository combines well-documented Python modules with Jupyter notebooks to demonstrate the complete workflow of MRI image acquisition and reconstruction using progressively more advanced techniques.

---

## Overview

Magnetic Resonance Imaging (MRI) acquires data in the frequency domain (k-space) rather than directly in image space. The quality, speed, and robustness of MRI depend heavily on how k-space is sampled and reconstructed.

This project investigates:

- Digital MRI phantoms
- Fourier Transform and inverse Fourier reconstruction
- k-space representation
- Cartesian MRI acquisition
- Accelerated MRI through Cartesian undersampling
- Radial MRI acquisition
- Golden-angle radial MRI
- Density compensation
- Simplified nearest-neighbor gridding reconstruction

The repository focuses on understanding the computational principles behind MRI rather than implementing clinically optimized reconstruction algorithms.

---

# Research Questions

This investigation addresses the following questions:

1. How are MRI images represented in k-space?

2. How does the Fourier Transform relate image space and frequency space?

3. How does Cartesian undersampling affect image quality?

4. How does radial MRI differ from Cartesian MRI?

5. What advantages does golden-angle radial sampling provide?

6. Why is density compensation necessary for radial MRI?

7. How can non-Cartesian k-space be reconstructed using gridding?

---

# Repository Structure

```
MRI-Reconstruction/
│
├── README.md
├── LICENSE
├── requirements.txt
│
├── src/
│   ├── phantom.py
│   ├── image_utils.py
│   ├── fft.py
│   ├── kspace.py
│   ├── cartesian_sampling.py
│   ├── radial_sampling.py
│   ├── golden_angle.py
│   └── gridding.py
│
├── notebooks/
│   ├── 01_digital_phantoms.ipynb
│   ├── 02_fourier_transform_and_kspace.ipynb
│   ├── 03_cartesian_sampling.ipynb
│   ├── 04_radial_sampling.ipynb
│   ├── 05_golden_angle_sampling.ipynb
│   └── 06_gridding_reconstruction.ipynb
│
└── images/
```

---

# Python Modules

## `phantom.py`

Generate analytical MRI phantoms for reconstruction experiments.

Features:

- Modified Shepp–Logan phantom
- Circular phantoms
- Rectangular phantoms
- Multiple-circle phantoms

---

## `image_utils.py`

Utility functions for image processing and visualization.

Features:

- Image normalization
- Image resizing
- Image comparison
- Image statistics
- Display utilities

---

## `fft.py`

Centered Fourier Transform utilities.

Features:

- Centered 2D FFT
- Centered inverse FFT
- Magnitude images
- Phase images

---

## `kspace.py`

Utilities for manipulating and analyzing MRI k-space.

Features:

- Log-magnitude visualization
- Center cropping
- Low-frequency removal
- High-frequency removal
- Energy computation

---

## `cartesian_sampling.py`

Simulation of Cartesian MRI acquisition.

Features:

- Cartesian sampling masks
- Uniform undersampling
- Sampling percentage
- Acceleration factor computation

---

## `radial_sampling.py`

Simulation of conventional radial MRI acquisition.

Features:

- Radial trajectories
- Radial sampling masks
- Radial k-space acquisition
- Zero-filled reconstruction

---

## `golden_angle.py`

Simulation of golden-angle radial MRI.

Features:

- Golden-angle trajectory generation
- Golden-angle sampling masks
- Interrupted acquisition experiments

---

## `gridding.py`

Simplified non-Cartesian MRI reconstruction.

Features:

- Trajectory sampling
- Sampling density maps
- Density compensation
- Nearest-neighbor gridding
- Image reconstruction

---

# Jupyter Notebooks

## Notebook 1 — Digital MRI Phantoms

Investigates analytical phantoms used for controlled MRI experiments.

Topics include:

- Shepp–Logan phantom
- Synthetic objects
- Image normalization
- Image comparison

---

## Notebook 2 — Fourier Transform and k-space

Introduces MRI image formation.

Topics include:

- Fourier Transform
- Inverse Fourier Transform
- k-space visualization
- Low-frequency information
- High-frequency information

---

## Notebook 3 — Cartesian MRI Sampling

Investigates accelerated Cartesian MRI.

Topics include:

- Cartesian undersampling
- Acceleration factors
- Aliasing artifacts
- Reconstruction quality

---

## Notebook 4 — Radial MRI

Investigates conventional radial MRI acquisition.

Topics include:

- Radial trajectories
- Radial sampling masks
- Streak artifacts
- Effect of increasing the number of spokes

---

## Notebook 5 — Golden-Angle MRI

Compares conventional radial MRI with golden-angle sampling.

Topics include:

- Uniform versus golden-angle trajectories
- Sampling distribution
- Interrupted acquisition
- Reconstruction comparison
- Error analysis

---

## Notebook 6 — Gridding Reconstruction

Introduces simplified non-Cartesian MRI reconstruction.

Topics include:

- Radial sampling density
- Density compensation
- Nearest-neighbor gridding
- Image reconstruction
- Quantitative evaluation (MSE, PSNR, SSIM)

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/MRI-Reconstruction.git

cd MRI-Reconstruction
```

Install the required packages

```bash
pip install -r requirements.txt
```

---

# Requirements

- Python 3.10+
- NumPy
- Matplotlib
- scikit-image

---

# Running the Notebooks

Launch Jupyter Notebook

```bash
jupyter notebook
```

or

```bash
jupyter lab
```

Open the notebooks in numerical order, beginning with:

```
01_digital_phantoms.ipynb
```

Each notebook builds upon concepts introduced in the previous notebook.

---

# Scientific Scope

This repository is intended as a computational investigation of MRI acquisition and reconstruction principles.

The implementations prioritize clarity and educational value over computational efficiency or clinical performance.

Several algorithms are intentionally simplified, including:

- Zero-filled reconstruction
- Radial density compensation
- Nearest-neighbor gridding

These simplified implementations illustrate the underlying concepts while motivating more advanced reconstruction methods used in modern MRI systems.

---

# Future Work

Possible extensions include:

- Kaiser–Bessel gridding
- Non-Uniform Fast Fourier Transform (NUFFT)
- Parallel MRI (SENSE)
- Parallel MRI (GRAPPA)
- Compressed sensing
- Deep-learning-based MRI reconstruction
- Dynamic MRI reconstruction
- Multi-coil MRI simulation

---

# References

- Haacke EM, Brown RW, Thompson MR, Venkatesan R. *Magnetic Resonance Imaging: Physical Principles and Sequence Design.*
- Bernstein MA, King KF, Zhou XJ. *Handbook of MRI Pulse Sequences.*
- Liang ZP, Lauterbur PC. *Principles of Magnetic Resonance Imaging.*
- Larson PEZ, Simonetti OP. *MRI Questions*.
- Beatty PJ, Nishimura DG, Pauly JM. Rapid gridding reconstruction with a minimal oversampling ratio.

---

# License

This project is released under the MIT License.

---

# Acknowledgments

This project was developed as an independent computational investigation into MRI acquisition and image reconstruction, with the goal of providing a clear, modular, and reproducible implementation of the core principles underlying modern MRI systems.