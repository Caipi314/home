# **__The call home TCP/TLS server__**
Devices will call this server on startup and optionally at a set interval.
It is designed to simplify the process of upgrading firmware, specifically to do so at convenient times.


# Expected Server Flow
1. On connection, the device sends a string of data that will be used to initiate an auto-upgrade.
2. Next, a firmware is found that is marked as current and has the same useCase and HWDevID as the device.
3. Then, if the device is not already running that firmware, the connection will be terminated and the firmware upgrade process will start.
4. The connection gets passed off to the `firmware.patch()` method

![Imgur](https://i.imgur.com/mfCwJQW.png)

## Aditionally
- For the firmware upgrade to start, the `parentId` and `_id` of the device need to be found.
- These data points are found by finding devices with the same IP address and `HWDevId` as the connected device.
- The IP address is specifically requested with the `WA` command; the `HWDevID` is sent by the device on connection.

### Sample sucess log
![Imgur](https://i.ibb.co/Ssf8r5t/sample.gif)

#### TODO
- User will be able to set which port the server runs on
- User will be able to start and stop the server through a GUI
