# Hand Gesture Controlled Mouse and Keyboard

This project enables you to control your computer's mouse and keyboard using hand gestures detected via a webcam. The project leverages OpenCV for image processing, Mediapipe for hand tracking, and Autopy for controlling the mouse and keyboard.

## Features

- **Hand Detection**: Uses Mediapipe to detect and track hands.
- **Mouse Control**: Move the mouse cursor and perform click actions using hand gestures.
- **Virtual Keyboard**: Display and use a virtual keyboard using hand gestures.

## Requirements

To run this project, you will need the following libraries:

- `opencv-python`
- `mediapipe`
- `numpy`
- `autopy`
- `cvzone`
- `pynput`
- `python version 3.8`

You can install these dependencies using pip:

```bash
pip install opencv-python mediapipe numpy autopy cvzone pynput
```

## File Overview

### HandDetector.py

This file contains the `HandDetector` class which is responsible for detecting and tracking hands using Mediapipe.

### MouseAndKbdControl.py

This file initializes the hand detector and uses it to control the mouse and virtual keyboard based on the detected hand gestures.

### VirtualKeyboardClass.py

This file contains the `VirtualKeyboard` class which is responsible for rendering the virtual keyboard and handling key press actions using hand gestures.

### VirtualMouseClass.py

This file contains the `VirtualMouse` class which is responsible for tracking the fingertip and controlling the mouse cursor and click actions using hand gestures.


## Usage

- **Activate Mouse Control**: Show all fingers to switch to mouse control mode.
- **Activate Keyboard Control**: Show only the pinky finger to switch to keyboard control mode.
- **Move Cursor**: In mouse control mode, keep only your index finger extended and move it to control the cursor's movement.
- **Click**: In mouse control mode, bring your index and middle fingers close together to perform a click.
- **Type**: In keyboard control mode, pinch the desired key with your index and middle fingers to type it.

## License

This project is open-source and available under the MIT License.
