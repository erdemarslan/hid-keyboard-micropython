# hid-keyboard-micropython
HID Keyboard extension for Raspberry Pi Pico with MicroPython

You can reset your Pico's memory with flash_nuke.uf2 file. Upload firmware_with_HID_support.v.1.17.uf2 firmware to your Raspberry Pi Pico. This firmware supports HID.

lib/keyboard.py file is noobeepi's hid keyboard extension. This extension use keyboard key's hex code to press or release keys. This hex codes not letters ascii hex codes. I put keys_hex_example.py file this repo. This is Turkish Q layout example. Other layouts maybe different but you can test it. Ascii letters must be same but others hex codes may little bit different. You can test it with main.py file.
