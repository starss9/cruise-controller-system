import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Streamlit UI
st.title(" Cruise Control System Simulator")
st.markdown("Tune the PID controller and observe how the system responds to a speed setpoint.")

# Sidebar sliders for PID gains
Kp = st.sidebar.slider("Proportional Gain (Kp)", 0, 1000, 500)
Ki = st.sidebar.slider("Integral Gain (Ki)", 0, 100, 10)
Kd = st.sidebar.slider("Derivative Gain (Kd)", 0, 500, 50)

# Car parameters
m = 1000  # kg
b = 50    # damping

# Plant transfer function
num = [1]
den = [m, b]
plant = ctrl.TransferFunction(num, den)

# PID controller
pid = ctrl.TransferFunction([Kd, Kp, Ki], [1, 0])

# Closed-loop system
system = ctrl.feedback(pid * plant)

# Simulation parameters
t = np.linspace(0, 20, 1000)
setpoint = 10  # m/s
_, y = ctrl.step_response(system * setpoint, t)

# Plotting
fig, ax = plt.subplots()
ax.plot(t, y, label="Speed (m/s)", linewidth=2)
ax.axhline(setpoint, color='r', linestyle='--', label='Setpoint (10 m/s)')
ax.set_title("System Step Response")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Speed (m/s)")
ax.legend()
ax.grid(True)

st.pyplot(fig)
