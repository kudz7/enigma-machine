import random
import string

class Plugboard:
    def __init__(self, swaps):
        self.swaps = swaps

class Rotors:
    def __init__(self, settings):
        self.settings = settings

class Enigma(Rotors, Plugboard):
    def __init__(self, swaps, settings):
        Plugboard.__init__(self, swaps)
        Rotors.__init__(self, settings)

    def increment(self):
        for i in range(0, len(self.settings)-1):
            if self.settings[(i%len(self.settings))-1] == 0:
                break
            else:
                temp = self.settings[(i%len(self.settings))-1]
                self.settings[(i%len(self.settings))-1] = self.settings[i]
                self.settings[i] = temp
        return self.settings

    def encrypt(self,i):
        alphabet = list(map(chr, range(97, 123)))
        index = alphabet.index(i)
        i = self.swap(self.settings[index])
        self.settings = self.increment()
        return i

    def decrypt(self,i):
        alphabet = list(map(chr, range(97, 123)))
        i = self.swap(i)
        index = self.settings.index(i)
        i = alphabet[index]
        self.settings = self.increment()
        return i
    
    def swap(self,n):
        for x in self.swaps:
            if n in x:
                for j in x:
                    if j != n:
                        n = j
                        break
        return n
    
    def encrypt_input(self, s):
        message = ""
        for i in s:
            if i != " ":
                message = message + self.encrypt(i)
        return message

    def decrypt_input(self, old_swaps, old_settings, e_input):
        message = ""
        self.reset(old_swaps, old_settings)
        for i in e_input:
            message = message + self.decrypt(i)
        return message

    def reset(self, old_swaps, old_settings):
        self.swaps = old_swaps
        self.settings = old_settings
    
a = string.ascii_lowercase
a = list(a)
random.shuffle(a)
s = [tuple(a[i:i+2]) for i in range(0, len(a), 2)]
e = Enigma(s, a)
        
