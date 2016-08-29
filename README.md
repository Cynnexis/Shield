# Shield - Network Guardian
Shield is a python script which can change your MAC address very quickly, by setting down/up the network interface automatically. The real advantage of using Shield is the MAC address prefix (the three hexadecimal number at the beginning of the MAC address) use the macchanger database to create a MAC address just like it was made by a real producer, to make your fake MAC address as real as possible.

## Downloading and installation:
       You just have to download the files "mac\_producer.list" and "shield.py". The file "mac\_producer" is not necessary. Actually, "mac\_producer.list" and "mac\_producer" are the same file, except "mac\_producer.list" is compiled by Pickle library. "shield.py" detect automatically if "mac\_producer.list" exists. If it does not, it will try to compile the database from "mac\_producer". But if there is neither "mac\_producer.list" nor "mac\_producer", the script cannot do anything and will exit. In other word, you just have to make sur there is either  "mac\_producer.list" or "mac\_producer" in the same directoy of "shield.py".

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

### Note:
       As a french developper who try to learn english, I think there is a LOT of mistake in those texts (also in the source code). So, you're welcome to warn me about it if you find one of them. Just let me know ;)
