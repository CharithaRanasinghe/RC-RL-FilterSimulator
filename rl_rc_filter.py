import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

dt = 0.01 
num_samples = 5000
noise_file = "noise.csv"

if not os.path.exists(noise_file):
    print(f"{noise_file} not found. Generating white Gaussian noise...")
    noise = np.random.normal(0, 1, num_samples)
    np.savetxt(noise_file, noise, delimiter=",")
    print(f"{noise_file} generated with {num_samples} samples.")
else:
    noise = np.loadtxt(noise_file, delimiter=",")
    print(f"{noise_file} loaded successfully.")

t = np.arange(len(noise)) * dt 

def rc_low_pass(x, dt, R, C):
    alpha = dt / (R * C + dt)
    y = np.zeros_like(x)
    for i in range(1, len(x)):
        y[i] = y[i - 1] + alpha * (x[i] - y[i - 1])
    return y


def rc_high_pass(x, dt, R, C):
    alpha = R * C / (R * C + dt)
    y = np.zeros_like(x)
    for i in range(1, len(x)):
        y[i] = alpha * (y[i - 1] + x[i] - x[i - 1])
    return y


def rl_low_pass(x, dt, R, L):
    alpha = dt / (L / R + dt)
    y = np.zeros_like(x)
    for i in range(1, len(x)):
        y[i] = y[i - 1] + alpha * (x[i] - y[i - 1])
    return y


def rl_high_pass(x, dt, R, L):
    alpha = dt / (L / R + dt)
    y = np.zeros_like(x)
    for i in range(1, len(x)):
        y[i] = (1 - alpha) * (y[i - 1] + x[i] - x[i - 1])
    return y

def cutoff_from_RC(R, C):
    return 1 / (2 * np.pi * R * C)


def cutoff_from_RL(R, L):
    return R / (2 * np.pi * L)
  
R_init = 1000
C_init = 1e-6
L_init = 1e-3


def update_filters(R, L, C):
    rc_lp = rc_low_pass(noise, dt, R, C)
    rc_hp = rc_high_pass(noise, dt, R, C)
    rl_lp = rl_low_pass(noise, dt, R, L)
    rl_hp = rl_high_pass(noise, dt, R, L)
    return [noise, rc_lp, rc_hp, rl_lp, rl_hp]


signals = update_filters(R_init, L_init, C_init)
titles = ["Original Signal", "RC Low-Pass", "RC High-Pass", "RL Low-Pass", "RL High-Pass"]

fig, axs = plt.subplots(5, 1, figsize=(12, 12))
plt.subplots_adjust(bottom=0.35, hspace=0.5)

lines = []
for ax, sig, title in zip(axs, signals, titles):
    line, = ax.plot(t, sig)
    ax.set_title(title)
    ax.set_xlabel("Time [s]")
    ax.set_ylabel("Amplitude")
    lines.append(line)

cutoff_texts = []
for ax, name in zip(axs[1:], ["RC", "RC", "RL", "RL"]):
    txt = ax.text(0.95, 0.85, "", transform=ax.transAxes, ha='right', fontsize=10, color='red')
    cutoff_texts.append(txt)


ax_R = plt.axes([0.25, 0.25, 0.50, 0.03])
ax_C = plt.axes([0.25, 0.20, 0.50, 0.03])
ax_L = plt.axes([0.25, 0.15, 0.50, 0.03])

slider_R = Slider(ax_R, "R (Ω)", 10, 10000, valinit=R_init, valstep=10)
slider_C = Slider(ax_C, "C (F, log)", np.log10(1e-9), np.log10(1e-3), valinit=np.log10(C_init))
slider_L = Slider(ax_L, "L (H, log)", np.log10(1e-6), np.log10(1), valinit=np.log10(L_init))

def update(val):
    R = slider_R.val
    C = 10 ** slider_C.val
    L = 10 ** slider_L.val

    updated = update_filters(R, L, C)
    for line, data_new in zip(lines, updated):
        line.set_ydata(data_new)
      
    cutoff_texts[0].set_text(f"f_c={cutoff_from_RC(R, C):.1f} Hz")
    cutoff_texts[1].set_text(f"f_c={cutoff_from_RC(R, C):.1f} Hz")
    cutoff_texts[2].set_text(f"f_c={cutoff_from_RL(R, L):.1f} Hz")
    cutoff_texts[3].set_text(f"f_c={cutoff_from_RL(R, L):.1f} Hz")

    fig.canvas.draw_idle()


slider_R.on_changed(update)
slider_C.on_changed(update)
slider_L.on_changed(update)

plt.show()
