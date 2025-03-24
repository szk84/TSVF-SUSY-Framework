# Bandpass filter the data to isolate the GW event clearly
gw150914_filtered = gw150914_data.bandpass(50, 250, filtfilt=True)

# Crop the data tightly around the GW150914 merger event
gw150914_event = gw150914_filtered.crop(1126259462.35, 1126259462.45)

# Plot the filtered and cropped strain data
plot = gw150914_event.plot()
plot.title = 'Filtered and Cropped GW150914 Event'
plot.xlabel = 'Time [seconds]'
plot.ylabel = 'Strain'
plot.show()
