## Overview

The Enigma Machine is an encryption device used by the Nazis during WW2. This code replicates the substitution cipher and allows the user to encrypt their plain text. The main class is Enigma, its parents are the classes Rotors and Plugboard which must be configured in order for Enigma to be used.

### Rotors

This object is simply an array of the 26 letters of the alphabet in lower case in the order you decide. These rotors are how letters will be encrypted.

### Plugboard

This is simply a list of 2-tuples of letters. If the letter that comes out of rotor encryption is paired in the plugboard object, it is swapped with the letter it's paired with.

## Enigma

This object is a child of both Rotors and Plugboard. As an input, it takes three rotor configurations and one plugboard setting. It has the following methods:

  <code>increment(self, rotor)</code> This takes a specific rotor as an inputs and increments it by one mod 26. So, letter 0 becomes letter 1, letter 1 becomes letter 2... letter 25 becomes letter 0.
  
  <code>encrypt(self,i)</code> This takes a specific letter as an input and encrypts it. The first rotor is then incremented by 1 position.
  
  <code>decrypt(self,i)</code> This take a specific letter as an input and decrypts it. The first rotor is then incremented by 1 position.
  
  <code>swap(self,n)</code> This take a specific letter as an input and checks to see if it has been connected with another letter on the pluboard. If it has, the input letter becomes the letter ithas been paired with after decryption.
  
  <code>encrypt_input(self, s)</code> This method takes the message as a string for the input _s_. It encrypts each letter. Every time the first rotor is incremented 26 times, the second rotor is incremented once. Every time the second rotor is incremented 26 times, the third rotor is incremented once.
  
  <code>decrypt_input(self, old_swaps, old_settings, old_settings2, old_settings3, e_input)</code> 
