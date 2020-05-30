import random
import string

#encryption must be in lower case

#this is the Plugboard class. This takes a list of 2-tuples. Each tuple is the two letters you want to swap together.
class Plugboard:
    def __init__(self, swaps):
        self.swaps = swaps
#this is the Rotors class. This must be a list of letters (strings). Each letter in the alphabet must be there.
class Rotors:
    def __init__(self, settings):
        self.settings = settings
        #error checking, there cannot be any duplicates, nonalpha characters or less than 26 letters
        if len(settings) != 26:
            raise Exception("Rotor must have 26 unique letters")
        if len(settings) != len(set(settings)):
            raise Exception("Rotor must have 26 unique letters")
        for i in settings:
            if i.isalpha() != True:
                raise Exception("Rotor must have 26 unique letters")

#this is the main machine, where the encryption happens
class Enigma(Rotors, Plugboard):
    def __init__(self, swaps, settings, settings2, settings3):
        Plugboard.__init__(self, swaps)
        self.settings = settings
        self.settings2 = settings2
        self.settings3 = settings3

#this function increments the rotor provided.
    def increment(self, rotor):
        for i in range(0, len(rotor)-1):
            if rotor[(i%len(rotor))-1] == 0:
                break
            else:
                temp = rotor[(i%len(rotor))-1]
                rotor[(i%len(rotor))-1] = rotor[i]
                rotor[i] = temp
        return rotor

#this function encrypts a single letter and increments the first rotor.
    def encrypt(self,i):
        alphabet = list(map(chr, range(97, 123)))
        index = alphabet.index(i)
        i = self.settings[index]
        index = alphabet.index(i)
        i = self.settings2[index]
        index = alphabet.index(i)
        i = self.swap(self.settings3[index])
        self.settings = self.increment(self.settings)
        return i

#this function decrypts a single letter and increments the first rotor.
    def decrypt(self,i):
        alphabet = list(map(chr, range(97, 123)))
        i = self.swap(i)
        index = self.settings3.index(i)
        i = alphabet[index]
        index = self.settings2.index(i)
        i = alphabet[index]
        index = self.settings.index(i)
        i = alphabet[index]
        self.settings = self.increment(self.settings)
        return i

#this function checks to see if the encrypted letter has been swapped on the plugboard. If so, it is swapped.    
    def swap(self,n):
        for x in self.swaps:
            if n in x:
                for j in x:
                    if j != n:
                        n = j
                        break
        return n

#this function encrypts an entire message. Every 26 times the first rotor is incremented, it increments the next rotor and so on.    
    def encrypt_input(self, s):
        message = ""
        fst_rotation = 0
        snd_rotation = 0
        trd_rotation = 0
        for i in s:
            if i != " ":
                message = message + self.encrypt(i)
                fst_rotation+=1
                if fst_rotation % 26 == 0:
                    self.settings2 = self.increment(self.settings2)
                    snd_rotation+=1
                    if snd_rotation % 26 == 0:
                        self.settings3 = self.increment(self.settings3)
                        trd_rotation+=1
        return message

#this function decrypts the entire message. The plugboard position, original 3 rotor positions in addition to the decrypted message must be provided. Every 26 times the first rotor is incremented, it increments the next rotor and so on.
    def decrypt_input(self, old_swaps, old_settings, old_settings2, old_settings3, e_input):
        message = ""
        fst_rotation = 0
        snd_rotation = 0
        trd_rotation = 0
        self.reset(old_swaps, old_settings, old_settings2, old_settings3)
        for i in e_input:
            message = message + self.decrypt(i)
            fst_rotation+=1
            if fst_rotation % 26 == 0:
                    self.settings2 = self.increment(self.settings2)
                    snd_rotation+=1
                    if snd_rotation % 26 == 0:
                        self.settings3 = self.increment(self.settings3)
                        trd_rotation+=1
        return message

#this function resets the rotor and swap settings for decryption. If the rotor and swap settings are correct, the message will be successfully decrypted.
    def reset(self, old_swaps, old_settings, old_settings2, old_settings3):
        self.swaps = old_swaps
        self.settings = old_settings
        self.settings2 = old_settings2
        self.settings3 = old_settings3
  
