# nethserver-box

This package is installed on all Nethesis appliances and has 2 different goals:

- creation of custom image: special crafted system-init which shutdown the machine after the first start
- multiple optimizations

## Optimizations

The package is well suited for installation on hardware with limited capacity, like APU devices from [PC Engines](https://www.pcengines.ch).
It applies the following configurations:

- ClamAV default signatures are always disabled
- fstrim service is enabled to improve SSD performance
- decrease swappiness to lower SSD I/O stress
- rebuild initramfs only for the current hardware to speedup dracut process
- enable serial console
