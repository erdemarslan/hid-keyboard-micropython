"""
HID Keyboard extension module for Raspberry Pi Pico with Micropython
Original Post: (noobeepi) https://forums.raspberrypi.com/viewtopic.php?t=310876&start=50

Original Github Page: https://github.com/noobee/micropython/tree/usb-hid
MicroPython with HID v1.17 flash file: https://forums.raspberrypi.com/download/file.php?id=50270&sid=d2380350c8264368b5c082ae68bafc40

Extension written by Erdem ARSLAN
erdemsaid[:at]gmail[dot]com

Github: https://github.com/erdemarslan/hid-keyboard-micropython

Please flash noobeepi's firmware to Pico before use.

version: v.1.0
"""
import keyboard

class hidkeyboard:
    
    k = keyboard.Keyboard()
    
    keys = {
        # Lowercase letters
        "a" : [0x04],
        "b" : [0x05],
        "c" : [0x06],
        "ç" : [0x37],
        "d" : [0x07],
        "e" : [0x08],
        "f" : [0x09],
        "g" : [0x0a],
        "ğ" : [0x2f],
        "h" : [0x0b],
        "ı" : [0x0c],
        "i" : [0x34],
        "j" : [0x0d],
        "k" : [0x0e],
        "l" : [0x0f],
        "m" : [0x10],
        "n" : [0x11],
        "o" : [0x12],
        "ö" : [0x36],
        "p" : [0x13],
        "q" : [0x14],
        "r" : [0x15],
        "s" : [0x16],
        "ş" : [0x33],
        "t" : [0x17],
        "u" : [0x18],
        "ü" : [0x30],
        "v" : [0x19],
        "w" : [0x1a],
        "x" : [0x1b],
        "y" : [0x1c],
        "z" : [0x1d],
        
        # Uppercase Letters
        "A" : [k.MOD_LEFT_SHIFT, 0x04],
        "B" : [k.MOD_LEFT_SHIFT, 0x05],
        "C" : [k.MOD_LEFT_SHIFT, 0x06],
        "Ç" : [k.MOD_LEFT_SHIFT, 0x37],
        "D" : [k.MOD_LEFT_SHIFT, 0x07],
        "E" : [k.MOD_LEFT_SHIFT, 0x08],
        "F" : [k.MOD_LEFT_SHIFT, 0x09],
        "G" : [k.MOD_LEFT_SHIFT, 0x0a],
        "Ğ" : [k.MOD_LEFT_SHIFT, 0x2f],
        "H" : [k.MOD_LEFT_SHIFT, 0x0b],
        "I" : [k.MOD_LEFT_SHIFT, 0x0c],
        "İ" : [k.MOD_LEFT_SHIFT, 0x34],
        "J" : [k.MOD_LEFT_SHIFT, 0x0d],
        "K" : [k.MOD_LEFT_SHIFT, 0x0e],
        "L" : [k.MOD_LEFT_SHIFT, 0x0f],
        "M" : [k.MOD_LEFT_SHIFT, 0x10],
        "N" : [k.MOD_LEFT_SHIFT, 0x11],
        "O" : [k.MOD_LEFT_SHIFT, 0x12],
        "Ö" : [k.MOD_LEFT_SHIFT, 0x36],
        "P" : [k.MOD_LEFT_SHIFT, 0x13],
        "Q" : [k.MOD_LEFT_SHIFT, 0x14],
        "R" : [k.MOD_LEFT_SHIFT, 0x15],
        "S" : [k.MOD_LEFT_SHIFT, 0x16],
        "Ş" : [k.MOD_LEFT_SHIFT, 0x33],
        "T" : [k.MOD_LEFT_SHIFT, 0x17],
        "U" : [k.MOD_LEFT_SHIFT, 0x18],
        "Ü" : [k.MOD_LEFT_SHIFT, 0x30],
        "V" : [k.MOD_LEFT_SHIFT, 0x19],
        "W" : [k.MOD_LEFT_SHIFT, 0x1a],
        "X" : [k.MOD_LEFT_SHIFT, 0x1b],
        "Y" : [k.MOD_LEFT_SHIFT, 0x1c],
        "Z" : [k.MOD_LEFT_SHIFT, 0x1d],
        
        # Numbers
        "0" : [0x27],
        "1" : [0x1e],
        "2" : [0x1f],
        "3" : [0x20],
        "4" : [0x21],
        "5" : [0x22],
        "6" : [0x23],
        "7" : [0x24],
        "8" : [0x25],
        "9" : [0x26],
        
        # Other Characters
        "!" : [k.MOD_LEFT_SHIFT, 0x1e],
        "'" : [k.MOD_LEFT_SHIFT, 0x1f],
        " " : [0x2c],
        "#" : [k.MOD_RIGHT_ALT, 0x20],
        "+" : [k.MOD_LEFT_SHIFT, 0x21],
        "$" : [k.MOD_RIGHT_ALT, 0x21],
        "%" : [k.MOD_LEFT_SHIFT, 0x22],
        "&" : [k.MOD_LEFT_SHIFT, 0x23],
        "/" : [k.MOD_LEFT_SHIFT, 0x24],
        "(" : [k.MOD_LEFT_SHIFT, 0x25],
        "[" : [k.MOD_RIGHT_ALT, 0x25],
        ")" : [k.MOD_LEFT_SHIFT, 0x26],
        "]" : [k.MOD_RIGHT_ALT, 0x26],
        "=" : [k.MOD_LEFT_SHIFT, 0x27],
        "{" : [k.MOD_RIGHT_ALT, 0x24],
        "}" : [k.MOD_RIGHT_ALT, 0x27],
        "*" : [0x2d],
        "?" : [k.MOD_LEFT_SHIFT, 0x2d],
        "-" : [0x2e],
        "_" : [k.MOD_LEFT_SHIFT, 0x2e],
        "," : [0x31],
        ";" : [k.MOD_LEFT_SHIFT, 0x31],
        "." : [0x38],
        ":" : [k.MOD_LEFT_SHIFT, 0x38],
        "@" : [k.MOD_RIGHT_ALT, 0x14],
        "<" : [0x64],
        ">" : [k.MOD_LEFT_SHIFT, 0x64],
        "|" : [k.MOD_RIGHT_ALT, 0x64],
        "\"": [0x35],
        "\\": [k.MOD_RIGHT_ALT, 0x2d]
        
        }
  
    def __init__(self):
        k = keyboard.Keyboard()
        
    def _find_char_and_send(self, character : str) -> None:
        global k;
        
        if character in self.keys:
            values = self.keys[character]
            
            if len(values) > 1:
                self.k.press(values[0], values[1])
            else:
                self.k.press(values[0])
            
            self.k.release_all()
    
    def write(self, string_data : str) -> None:
        for s in string_data:
            self._find_char_and_send(s)
        