## Overview

The Enigma Machine is an encryption device used by the Nazis during WW2. This code replicates the substitution cipher and allows the user to encrypt their plain text. The main class is Enigma, its parents are the classes Rotors and Plugboard which must be configured in order for Enigma to be used.

### Rotors

This object is simply an array of the 26 letters of the alphabet in lower case in the order you decide. These rotors are how letters will be encrypted.

### Plugboard

This is simply a list of 2-tuples of letters. If the letter that comes out of rotor encryption is paired in the plugboard object, it is swapped with the letter it's paired with.
