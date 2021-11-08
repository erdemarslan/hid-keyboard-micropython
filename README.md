# hid-keyboard-micropython
HID Keyboard extension for Raspberry Pi Pico with MicroPython

You can reset your Pico's memory with flash_nuke.uf2 file. Upload firmware_with_HID_support.v.1.17.uf2 firmware to your Raspberry Pi Pico. This firmware supports HID.

lib/keyboard.py file is noobeepi's hid keyboard extension. With this extension you can send only char which known ascii code. This extension use keyboard key's hex code to press or release keys. This hex codes not letters hex codes, keyboard keys hex code. I wrote lib/klavye.py extension to send strings.

In keys_hex_example.py file you can see keyboard key hex code example. This example for Turkish Q layout keyboards. Other layouts maybe different but you can test it with main.py file.
