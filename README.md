![R-SODIUM-Ultra-Enclosure-Manager](https://socialify.git.ci/barryblueice/R-SODIUM-Ultra-Enclosure-Manager/image?font=JetBrains+Mono&logo=https%3A%2F%2Fdl.barryblueice.cn%2Fdownload%2Frsodium-ultra-enclosure-manager-icon.png&name=1&pattern=Signal&theme=Auto)
<p align="center">
  <img alt="GitHub License" src="https://img.shields.io/github/license/barryblueice/R-SODIUM-Ultra-Enclosure-Manager">
</p>

## **简介：**
基于Python+Pyside6的R-SODIUM Ultra Enclosure GUI控制端。

<img width="518" height="419" alt="image" src="https://github.com/user-attachments/assets/cbfcdd19-89da-4342-b14c-a581ac8c6cbf" />

## **协议：**
`R-SODIUM Ultra Enclosure Manager`遵循[Mozilla Public License 2.0](https://github.com/barryblueice/R-SODIUM-Ultra-Enclosure-Manager?tab=MPL-2.0-1-ov-file)协议开源。如需自定义源码并二次分发，请明确标明原出处。
## **硬件开源地址：**

[USB 10Gbps多协议三盘盒 VL822+ESP32](https://oshwhub.com/barryblueice/usb-multi-protocol-three-disk-bo)

## **工作原理：**

将ESP32-S2模拟为自定义HID设备，通过自定义HID报文通信控制ESP32 GPIO状态：

<img width="1371" height="591" alt="image" src="https://github.com/user-attachments/assets/88ab1ec5-0385-47ef-8ca2-fc09b6b35060" />

[ESP-IDF开发USB HID设备记录（3）——ESP32开发自定义HID设备，通过HID报文通信](https://www.bilibili.com/opus/1093492407233675281)</br>
[ESP-IDF开发USB HID设备记录（4）——利用HMAC-SHA256给自定义报文加“料”](https://www.bilibili.com/opus/1093956714689986579)
