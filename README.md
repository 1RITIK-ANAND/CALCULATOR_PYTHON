
# Calculator 

This is a simple calculator application built using Python's `Tkinter` library. It includes basic arithmetic operations, keyboard input support, and a feature to toggle between dark and light themes. 

## Features

- **Basic Calculator Operations**: Supports addition, subtraction, multiplication, division, and more.
- **Clear & Backspace**: Functions to clear the input field and remove the last character.
- **Sign Toggle**: Ability to toggle the sign of the number (positive/negative).
- **Keyboard Support**: Input calculations directly from the keyboard.
- **Theme Switching**: Toggle between a dark theme and light theme for better user experience.
- **Hover Effects**: Buttons change color when hovered over to enhance the UI interaction.

## Requirements

- Python 3.x
- Tkinter (Usually comes with the standard Python distribution)

## Installation

1. Install Python from the official website: https://www.python.org/downloads/
   
   Tkinter comes bundled with Python, so you don't need to install it separately.

2. Save the provided code into a `.py` file, for example `calculator.py`.

3. Run the file using Python:

   ```bash
   python calculator.py
   ```

## Usage

- **Basic Operations**: Click on the digits and arithmetic operators to perform calculations.
- **Clear**: The "C" button clears the input field.
- **Backspace**: The "⌫" button removes the last character entered.
- **Sign Toggle**: The "±" button toggles the sign of the current value in the input field.
- **Theme Toggle**: The "Theme" button switches between the dark and light theme.

You can also enter values and operations via the keyboard, and press **Enter** to evaluate the expression.

## Example

1. Enter `3 + 5` and click `=`, it will display `8`.
2. Enter `12 / 4` and click `=`, it will display `3`.
3. Press `±` to toggle the sign of a number.
4. Press `Theme` to switch between light and dark themes.

## Code Overview

- **Main Colors**: 
  - `ORANGE`: Used for the buttons' default background.
  - `DARK_ORANGE`: Used when hovering over the buttons.
  - `BLACK` and `WHITE`: Background and text color for the themes.

- **Functions**:
  - `on_enter(e)`: Handles the hover effect for buttons.
  - `on_leave(e)`: Reverts the hover effect when the mouse leaves the button.
  - `click(event)`: Handles button clicks for arithmetic operations.
  - `key_input(event)`: Allows input via the keyboard.
  - `toggle_theme()`: Switches between dark and light themes.

## Example Screenshots

- Dark Theme:

  ![CALC](https://github.com/user-attachments/assets/b866e6c3-4309-4470-9460-a02de35abe33)





- Light Theme:

  ![WHITE](https://github.com/user-attachments/assets/caf25b7e-57cb-4280-bd28-eefcfa723e56)

