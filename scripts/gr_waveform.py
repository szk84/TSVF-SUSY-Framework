from pycbc.waveform import get_td_waveform
import matplotlib.pyplot as plt

# Generate GR waveform
hp_gr, _ = get_td_waveform(
    approximant="TaylorT4",
    mass1=30,
    mass2=30,
    delta_t=1.0/4096,
    f_lower=20,
    distance=100
)

# Center time at merger (convert LIGOTimeGPS to float)
end_time_seconds = hp_gr.end_time.gpsSeconds
time = hp_gr.sample_times - end_time_seconds

# Plot waveform around merger
plt.figure(figsize=(10, 6))
plt.plot(time, hp_gr, 'b-', lw=1.5)
plt.xlim(-0.5, 0.1)
plt.xlabel('Time (s) from Merger', fontsize=12)
plt.ylabel('Strain', fontsize=12)
plt.title(r'Gravitational Waveform (30M$_\odot$–30M$_\odot$ Binary Black Hole)', fontsize=14)
plt.grid(alpha=0.3)
plt.savefig('gr_waveform.png', dpi=300, bbox_inches='tight')
plt.close()