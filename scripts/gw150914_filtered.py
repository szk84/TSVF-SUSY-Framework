import matplotlib
matplotlib.use('Qt5Agg')

from gwpy.timeseries import TimeSeries

# Retrieve GW150914 data clearly
gw150914_data = TimeSeries.fetch_open_data('H1', 1126259462, 1126259478, cache=True)

# Filter and crop the data around the event
gw150914_filtered = gw150914_data.bandpass(50, 250, filtfilt=True)
gw150914_event = gw150914_filtered.crop(1126259462.35, 1126259462.45)

# Compute ASD clearly
asd = gw150914_event.asd(fftlength=0.1, overlap=0.05)

# Plot ASD clearly
plot = asd.plot()
plot.title = 'GW150914 Amplitude Spectral Density'
plot.xlim(0, 500)
plot.xlabel = 'Frequency [Hz]'
plot.ylabel = 'Strain [Hz$^{-1/2}$]'
plot.show()
