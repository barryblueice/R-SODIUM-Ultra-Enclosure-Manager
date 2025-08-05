<p align="center">
  <img width="1280" height="640" alt="image" src="https://github.com/user-attachments/assets/19ffe58d-2d4c-4a41-be81-c2a7d45c923f" />
  <img alt="GitHub License" src="https://img.shields.io/github/license/barryblueice/R-SODIUM-Ultra-Enclosure-Manager">
</p>

## **简介：**
基于Python+Pyside6的R-SODIUM Ultra Enclosure GUI控制端。

<img width="509" height="423" alt="image" src="https://github.com/user-attachments/assets/f2bd080a-25d7-4438-a49b-ed5ae81653a1" />

## **协议：**
`R-SODIUM Ultra Enclosure Manager`遵循[Mozilla Public License 2.0](https://github.com/barryblueice/R-SODIUM-Ultra-Enclosure-Manager?tab=MPL-2.0-1-ov-file)协议开源。如需自定义源码并二次分发，请明确标明原出处。

## **硬件开源地址：**

[USB 10Gbps多协议三盘盒 VL822+ESP32](https://oshwhub.com/barryblueice/usb-multi-protocol-three-disk-bo)

## **适用硬件设备：**
 - R-SODIUM Ultra Enclosure 1.0（第一代R-SODIUM Ultra Enclosure硬盘盒）。[固件下载地址←](https://github.com/barryblueice/R-SODIUM-Ultra-Enclosure-1.0-Firmware)
> [!CAUTION]
仅适用第一代ESP32版本，第一代8051版本不再提供任何技术支持。

## **工作原理：**

将ESP32-S2模拟为自定义HID设备，通过自定义HID报文通信控制ESP32 GPIO状态：

<img width="1371" height="591" alt="image" src="https://github.com/user-attachments/assets/88ab1ec5-0385-47ef-8ca2-fc09b6b35060" />

[ESP-IDF开发USB HID设备记录（3）——ESP32开发自定义HID设备，通过HID报文通信](https://www.bilibili.com/opus/1093492407233675281)</br>
[ESP-IDF开发USB HID设备记录（4）——利用HMAC-SHA256给自定义报文加“料”](https://www.bilibili.com/opus/1093956714689986579)
