from machine import Pin
from time import sleep

s_dot = 1
s_dash = 3
s_dot_dash = 1
s_letter = 1
s_space = 4

led = led = Pin(15, Pin.OUT)

def blink_dot():         
        led.on()
        sleep(s_dot)
        led.off()
        sleep(s_dot_dash)

def blink_dash():          
        led.on()
        sleep(s_dash)
        led.off()
        sleep(s_dot_dash)
        
def main():
        morse = {'A' : '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
                 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
                 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',  'O': '---', 
                 'P': '.--.','Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
                 'U': '..-', 'V': '...-', 'W': '.--',  'X': '-..-', 'Y': '-.--',   'Z': '--..',
                 '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', 
                 '5': '.....','6': '-....',  '7': '--...',  '8': '---..', '9': '----.',
                 ' ': '/'}
              
        message = input("Enter your message: ").upper()
        
        message_morse = []

        for symbol in message:                
                message_morse.append(morse[symbol])
                
        print(message_morse)
                    
        for i in message_morse:
                if i == '/':
                        sleep(s_space)
                else:
                        for j in i:
                                if j == '.':
                                        blink_dot()                                       
                                else:                                       
                                        blink_dash()                        
                        sleep(s_letter)
              
main()