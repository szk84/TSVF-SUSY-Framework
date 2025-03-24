from gwpy.timeseries import TimeSeries

# Retrieve GW150914 data from LIGO Hanford (H1)
gw150914_data = TimeSeries.fetch_open_data('H1', 1126259462, 1126259478, cache=True)

# Plot the strain data
plot = gw150914_data.plot()
plot.title = 'LIGO Hanford (H1) Strain Data for GW150914'
plot.xlabel = 'Time [s] from 1126259462'
plot.ylabel = 'Strain'
plot.show()
