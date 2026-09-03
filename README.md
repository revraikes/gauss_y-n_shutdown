# gauss_y-n_shutdown
## Sense HAT Gaussmeter with extras controllable by the joystick for a headless Pi using a battery powersource
### Features
- Gaussmeter  
- Smiley-face  
- Dead-face  
- Clear pixels  
- System shutdown

This project was developed to educate myself on Python programming. If you're anything like me, you need to see real results, and one of the more fun ways to do that is with flashy lights that also serve a valuable function. None of the available examples out in the wild had a function-switching capability, so I set about making that happen.

It was created on a Raspberry Pi 4 that I had lying around and using an Anker Power Bank battery, because a gaussmeter tied to an outlet isn't very useful (yes, it powers it just fine, but maybe not a Pi 5- YMMV).

The directions button in the .py file are written in a way that makes sense to me because the board is displayed upside down from the Sense HAT board's natural alignment due to the power source input being directly under that alignment and I want to have it sit on a table to show the smiley/dead faces for feedback to someone across from me. That also means the pixels are set "upside down" for those faces.

Lastly, there's a clear pixels function to save power and/or remove your face gesture, and pressing down in the middle shuts the Pi down so that just pulling the power doesn't damage the board or SD card.

Since the Pi is headless, I've included an installer script to make the application start on boot as a systemctl enabled service. Just navigate to the repo folder in terminal and type "./install-as-service.sh". To stop the service: "sudo systemctl stop gauss-tns.service".

h/t to [MadTC Tech](https://gitlab.com/MadTcTutorials/python/sensehat) for his invaluable examples and thorough video tutorials on Youtube
