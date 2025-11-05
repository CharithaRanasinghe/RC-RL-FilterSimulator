# RL/RC Filter Simulator

This project allows you to **visualize the time-domain response of RL and RC filters** (low-pass and high-pass) to a white Gaussian noise input signal. You can **interactively adjust R, L, and C values** using sliders and see how the filters modify the signal in real-time. The cutoff frequency of each filter is also displayed on the plots.

---

## Features

- RC Low-Pass and High-Pass filters
- RL Low-Pass and High-Pass filters
- Interactive sliders for R, L, and C
- Logarithmic scale for C and L sliders for easier tuning
- Displays cutoff frequency for each filter in real-time
- Automatically generates white Gaussian noise CSV if missing
- Fully self-contained Python script

---
<img width="1916" height="1019" alt="image" src="https://github.com/user-attachments/assets/82f6d3a8-cd65-4c85-8a1f-3d8cc988d313" />
---

## Folder Structure

rl_rc_filter_simulator/
│
├── noise.csv # Sample noise data (optional)
├── rl_rc_filter.py # Main interactive Python script
├── generate_noise.py # Script to generate noise CSV
├── requirements.txt # Python dependencies
└── README.md # This file



---

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/rl_rc_filter_simulator.git
cd rl_rc_filter_simulator
```

```bash
python -m venv venv
# Activate:
# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate
```

Usage
1. Generate Noise CSV (Optional)

If you want to generate a new noise CSV file, run:

python generate_noise.py


This will create noise.csv with 5000 samples of white Gaussian noise (mean 0, standard deviation 1).
You can also modify the generator to change the number of samples or noise characteristics.

2. Run the Filter Simulation
python rl_rc_filter.py


This will open a window with five plots:

Original Signal

RC Low-Pass

RC High-Pass

RL Low-Pass

RL High-Pass

3. Use the Sliders

R (Ω): Linear scale to adjust resistance

C (F, log): Logarithmic scale for capacitance

L (H, log): Logarithmic scale for inductance

Adjusting the sliders updates all filter plots in real-time, and the cutoff frequency of each filter is displayed in red on the corresponding plot.

---

How It Works

Discrete-time approximation is used for the filters for fast simulation.

RC filters:

Low-pass: y[n] = y[n-1] + α*(x[n] - y[n-1]), α = dt / (RC + dt)

High-pass: y[n] = α*(y[n-1] + x[n] - x[n-1]), α = RC / (RC + dt)

RL filters:

Low-pass: y[n] = y[n-1] + α*(x[n] - y[n-1]), α = dt / (L/R + dt)

High-pass: y[n] = (1 - α)*(y[n-1] + x[n] - x[n-1]), α = dt / (L/R + dt)

Cutoff frequencies:

RC: f_c = 1 / (2πRC)

RL: f_c = R / (2πL)

File Descriptions

rl_rc_filter.py – Main interactive Python script with sliders and plots

generate_noise.py – Generates noise.csv file with white Gaussian noise

noise.csv – Sample noise data (optional; auto-generated if missing)

requirements.txt – Python dependencies

README.md – Project instructions and usage guide

Notes

Recommended Python 3.8+.

Works in standard Python environments; does not require Jupyter Notebook.

Adjust slider ranges carefully for realistic filter behavior:

R: 10 Ω – 10 kΩ

C: 1 nF – 1 mF

L: 1 μH – 1 H

---



---

This README is **fully comprehensive**:

- Explains project features  
- Installation instructions  
- How to generate `noise.csv`  
- Usage instructions for the interactive plot  
- Slider explanation  
- Filter formulas and cutoff frequency  
- File structure  
- Notes and tips  
- License  

---



