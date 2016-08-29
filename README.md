# Shield - Network Guardian
Shield is a python script which can change your MAC address very quickly, by setting down/up the network interface automatically. The real advantage of using Shield is the MAC address prefix (the three hexadecimal number at the beginning of the MAC address) use the macchanger database to create a MAC address just like it was made by a real producer, to make your fake MAC address as real as possible.

## Usage:
       shield.py [change | reset] INTERFACE

## Description:
       change INTERFACE    Change INTERFACE mac address.
       reset  INTERFACE    Reset INTERFACE mac address.

## Examples:
       // Assuming wlan0 as network interface
       shield.py change wlan0 // Change wlan0 mac address.
       shield.py reset wlan0  // Reset wlan0 mac address.

## See also:
       ifconfig (8)

## Author:
       Valentin Berger <valentin.berger38@gmail.com>
