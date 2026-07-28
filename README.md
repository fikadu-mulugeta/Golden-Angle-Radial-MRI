# Golden Angle Radial MRI Acquisition and Reconstruction

A computational investigation into Magnetic Resonance Imaging (MRI) acquisition and image reconstruction, with a primary focus on radial MRI and golden-angle sampling.

The repository develops the computational foundations required to understand modern non-Cartesian MRI acquisition, beginning with digital phantom generation, Fourier Transform, k-space representation, and Cartesian MRI before progressing to radial trajectories, golden-angle sampling, density compensation, and simplified gridding reconstruction.

The project combines modular Python implementations with Jupyter notebooks to provide a clear, reproducible, and well-documented exploration of MRI acquisition and reconstruction principles.

---

## Repository

**GitHub Repository**

https://github.com/fikadu-mulugeta/Golden-Angle-Radial-MRI-Acquisition-and-Reconstruction

---

# Overview

Magnetic Resonance Imaging (MRI) acquires data in the frequency domain (k-space) rather than directly in image space. The quality, speed, and robustness of MRI depend heavily on how k-space is sampled and reconstructed.

This project investigates the complete computational workflow underlying MRI acquisition and reconstruction, including:

- Digital MRI phantoms
- Fourier Transform and inverse Fourier reconstruction
- k-space representation and visualization
- Cartesian MRI acquisition
- Accelerated MRI through Cartesian undersampling
- Conventional radial MRI acquisition
- Golden-angle radial MRI
- Density compensation
- Simplified nearest-neighbor gridding reconstruction

Although the primary emphasis is on golden-angle radial MRI, the repository first establishes the fundamental concepts of MRI image formation before introducing increasingly advanced acquisition and reconstruction techniques.

The implementations prioritize conceptual understanding, reproducibility, and modular software design rather than clinically optimized reconstruction algorithms.

---

# Motivation

Modern MRI systems increasingly rely on non-Cartesian acquisition strategies to improve acquisition efficiency, reduce motion artifacts, and enable accelerated imaging. Among these techniques, golden-angle radial sampling has become particularly important for dynamic and free-breathing MRI because it provides flexible and nearly uniform k-space coverage regardless of the number of acquired spokes.

Understanding these methods requires knowledge of MRI physics, Fourier Transform, k-space, sampling trajectories, and reconstruction algorithms. This repository brings these concepts together into a single computational project implemented entirely in Python.

---

# Objectives

The objectives of this project are to:

- Understand MRI image formation using the Fourier Transform.
- Explore the relationship between image space and k-space.
- Investigate Cartesian MRI acquisition and undersampling.
- Simulate radial MRI acquisition.
- Study golden-angle radial sampling.
- Visualize sampling trajectories.
- Investigate sampling density and density compensation.
- Implement simplified non-Cartesian gridding reconstruction.
- Evaluate reconstruction quality using quantitative image quality metrics.

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
Golden-Angle-Radial-MRI-Acquisition-and-Reconstruction/
│
├── README.md
├── LICENSE
├── CITATION.cff
├── requirements.txt
├── .gitignore
│
├── src/
│   ├── __init__.py
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

```

---

# Python Modules

## `phantom.py`

Generates analytical MRI phantoms for reconstruction experiments.

Features

- Modified Shepp–Logan phantom
- Circular phantoms
- Rectangular phantoms
- Multiple-circle phantoms

---

## `image_utils.py`

General-purpose image processing utilities.

Features

- Image normalization
- Image resizing
- Image visualization
- Image comparison
- Image statistics

---

## `fft.py`

Centered Fourier Transform utilities used throughout the repository.

Features

- Centered 2D Fast Fourier Transform
- Centered inverse Fourier Transform
- Magnitude visualization
- Phase visualization

---

## `kspace.py`

Utilities for manipulating and analyzing MRI k-space.

Features

- Log-magnitude visualization
- Center cropping
- Low-frequency removal
- High-frequency removal
- Energy computation

---

## `cartesian_sampling.py`

Simulation of Cartesian MRI acquisition and undersampling.

Features

- Cartesian sampling masks
- Uniform undersampling
- Sampling percentage computation
- Effective acceleration factor

---

## `radial_sampling.py`

Simulation of conventional radial MRI acquisition.

Features

- Radial trajectory generation
- Radial sampling masks
- Radial k-space acquisition
- Zero-filled reconstruction

---

## `golden_angle.py`

Simulation of golden-angle radial MRI acquisition.

Features

- Golden-angle trajectory generation
- Golden-angle sampling masks
- Interrupted acquisition experiments
- Progressive k-space coverage

---

## `gridding.py`

Simplified non-Cartesian MRI reconstruction.

Features

- Radial k-space sampling
- Sampling density estimation
- Density compensation
- Nearest-neighbor gridding
- Image reconstruction

---

# Jupyter Notebooks

The repository is organized as a sequence of Jupyter notebooks that progressively introduce MRI acquisition and reconstruction concepts.

## 01 — Digital Phantoms

Topics

- Digital image representation
- MRI phantoms
- Modified Shepp–Logan phantom
- Image visualization

---

## 02 — Fourier Transform and k-Space

Topics

- Two-dimensional Fourier Transform
- Inverse Fourier Transform
- Frequency domain representation
- k-space visualization
- Low- and high-frequency information

---

## 03 — Cartesian Sampling

Topics

- Cartesian MRI acquisition
- Undersampling
- Aliasing
- Acceleration factor
- Zero-filled reconstruction

---

## 04 — Radial Sampling

Topics

- Radial k-space trajectories
- Projection acquisition
- Radial reconstruction
- Comparison with Cartesian MRI

---

## 05 — Golden-Angle Sampling

Topics

- Golden-angle trajectory generation
- Progressive k-space coverage
- Flexible reconstruction
- Interrupted acquisition
- Dynamic MRI motivation

---

## 06 — Gridding Reconstruction

Topics

- Density compensation
- Non-Cartesian interpolation
- Nearest-neighbor gridding
- Image reconstruction
- Reconstruction quality evaluation

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/fikadu-mulugeta/Golden-Angle-Radial-MRI-Acquisition-and-Reconstruction.git

cd Golden-Angle-Radial-MRI-Acquisition-and-Reconstruction
```

## Create a Virtual Environment (Optional)

Windows

```bash
python -m venv venv

venv\Scripts\activate
```

Linux/macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements

- Python 3.10 or later
- NumPy
- Matplotlib
- scikit-image

---

# Running the Project

Launch Jupyter Notebook:

```bash
jupyter notebook
```

or JupyterLab:

```bash
jupyter lab
```

Then execute the notebooks in numerical order:

1. Digital Phantoms
2. Fourier Transform and k-Space
3. Cartesian Sampling
4. Radial Sampling
5. Golden-Angle Sampling
6. Gridding Reconstruction

Each notebook builds upon concepts introduced in the previous one.

---

# Results

The project demonstrates:

- Digital phantom generation
- Fourier-based MRI image formation
- k-space visualization
- Cartesian sampling and undersampling
- Radial MRI acquisition
- Golden-angle radial trajectories
- Density compensation
- Simplified gridding reconstruction
- Quantitative image quality evaluation using metrics such as PSNR and SSIM

---

# Scientific Scope

This repository is intended as an educational and computational investigation into MRI acquisition and reconstruction.

The implementations emphasize conceptual clarity and reproducibility rather than clinical optimization. In particular, the non-Cartesian reconstruction uses a simplified nearest-neighbor gridding approach designed to illustrate the principles of radial MRI reconstruction.

The project does **not** aim to replace advanced reconstruction techniques used in modern clinical MRI systems.

---

# Future Directions

Possible extensions include:

- Kaiser–Bessel gridding
- Non-Uniform Fast Fourier Transform (NUFFT)
- Parallel MRI (SENSE)
- Parallel MRI (GRAPPA)
- Compressed sensing MRI
- Multi-coil MRI simulation
- Motion correction
- Dynamic MRI reconstruction
- Deep learning-based MRI reconstruction
- Quantitative MRI applications

---

# References

The computational methods presented in this repository are based on established MRI literature, including textbooks and peer-reviewed publications on MRI physics, image reconstruction, Fourier imaging, and non-Cartesian sampling.

Representative references include:

- Bernstein MA, King KF, Zhou XJ. *Handbook of MRI Pulse Sequences*. Elsevier.
- Haacke EM, Brown RW, Thompson MR, Venkatesan R. *Magnetic Resonance Imaging: Physical Principles and Sequence Design*.
- Larson PEZ, Nishimura DG. *Stanford MRI Reconstruction Notes*.
- Pipe JG. Sampling density compensation in MRI.
- Winkelmann S, Schaeffter T, Koehler T, Eggers H, Doessel O. An optimal radial profile order based on the Golden Ratio for time-resolved MRI.

---

# Author

**Fikadu Mulugeta Gassa**

M.Sc. Biomedical Engineering

Research Interests

- MRI Acquisition and Reconstruction
- Medical Image Analysis
- MR Spectroscopy
- Machine Learning for Medical Imaging
- Biomedical Signal and Image Processing

GitHub

https://github.com/fikadu-mulugeta

---

# Citation

If you use this repository in your research, teaching, or other scholarly work, please cite it using the metadata provided in `CITATION.cff`.

---

# License

This project is licensed under the MIT License.

See the `LICENSE` file for details.

---

# Acknowledgments

This repository was developed as an independent computational investigation into the principles of Magnetic Resonance Imaging (MRI) acquisition and reconstruction. It integrates concepts from MRI physics, Fourier imaging, k-space analysis, Cartesian and radial sampling, golden-angle acquisition, and simplified non-Cartesian reconstruction into a cohesive educational resource implemented in Python.

The project is intended to support students, researchers, and practitioners seeking a practical understanding of MRI acquisition and reconstruction through reproducible computational experiments.

---

**If you find this repository useful, consider giving it a ⭐ on GitHub.**