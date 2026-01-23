# HnR'26 hardware badge: NFC controller hardware source files

This directory contains the [KiCad](https://www.kicad.org/) 9 hardware source
files for the Hack&Roll 2026 hardware badge NFC controller.

This NFC controller is used to track participant statistics during food
collection by using NFC communication to scan the participant badges. It can be
extended on to track event statistics during Hack&Roll 2026 as well.

## Manufacturing

We used [JLCPCB manufacturing services](https://jlcpcb.com/) for the hardware
badges. To help with generating JLCPCB-compatible files, we used the open source
[KiCad JLCPCB tools](https://github.com/bouni/kicad-jlcpcb-tools) plugin.

## License

The hardware source files in this directory are open-sourced, licensed under
CERN-OHL-P-2.0. See [LICENSE.md](./LICENSE.md) for the full license text.

## Acknowledgements

This Hack&Roll 2026 NFC controller hardware badge would not have been possible
without the following people:

- **Terence** Chan Zun Mun ([@Hackin7](https://github.com/Hackin7)), for his
  invaluable knowledge and guidance in PCB design and hardware badge
  development, as well as liaising with Espressif Systems
- Tan **Le Yew** ([@itsme-zeix](https://github.com/itsme-zeix)), for helping out
  with development and troubleshooting of the NFC controller badge
- Lim **Yik Jin** ([@yikjin](https://github.com/yikjin)), for developing the
  hardware badges
- Park **Youngseo** ([@youngseopark05](https://github.com/youngseopark05)), for
  creating the artwork used for this hardware badge
- Koh Chan Hong, **Ravern** ([@ravern](https://github.com/ravern)), for liaising
  with Espressif Systems
- Tan Rongwen, **Daren** ([@darentanrw](https://github.com/darentanrw)), for
  liaising with Espressif Systems
- Everyone in [NUS Hackers](https://www.nushackers.org/) for making Hack&Roll
  2026 a reality!

The ESP32-C3-WROOM-02-N4 module in the main hardware badge is also sponsored by
[Espressif Systems](https://www.espressif.com/), the manufacturers of the
widely-used ESP32 chips.
