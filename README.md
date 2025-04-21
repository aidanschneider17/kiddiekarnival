# Kiddie Karnival - LED Matrix Pong

## Overview

LED Matrix Pong is a simple, single-player Pong game specifically designed for children. Instead of a traditional screen, the game is intended to be displayed on a 64x64 RGB LED Matrix panel, controlled by a Raspberry Pi. The player controls a paddle using keyboard inputs to bounce a ball back.

The current Python code uses `pygame` to simulate the game logic and display, providing a foundation for driving the actual LED matrix hardware.

## Features

*   **Simple Pong Gameplay:** Easy-to-understand single-player Pong mechanics.
*   **Child-Friendly:** Designed with simple controls and clear visuals (Red ball, Blue paddle).
*   **Hardware Target:** Built for display on a 64x64 RGB LED Matrix via Raspberry Pi.
*   **Player Control:** Use UP and DOWN arrow keys to move the paddle vertically.
*   **Basic Physics:** Ball bounces off the top/bottom walls and the player's paddle.
*   **Paddle Collision Logic:** The angle the ball bounces off the paddle depends on where it hits (upper or lower half).

## Hardware Requirements

*   **Raspberry Pi:** Raspberry Pi 4 Model B (recommended) or a similar compatible model.
*   **LED Matrix:** 64x64 RGB LED Matrix Panel.
*   **Controller HAT:** An Adafruit RGB Matrix HAT + RTC for Raspberry Pi (or a similar compatible driver board/HAT/Bonnet).
*   **Power Supply:** A robust 5V power supply capable of powering *both* the Raspberry Pi and the LED Matrix (Matrices can draw significant current!).
*   **Input:** A standard USB Keyboard connected to the Raspberry Pi (Can also use a Raspberry Pi Pico with buttons wired up).
*   **Wiring:** Appropriate ribbon cables and connectors for the matrix and HAT.

## Software Requirements

*   **Operating System:** Raspberry Pi OS (or other compatible Linux distribution).
*   **Python:** Python 3.9 or higher.
*   **Libraries:**
    *   `pygame`: Used for game loop management, event handling (keyboard input), timing, and the current simulation display. Install using:
        ```bash
        pip install pygame
        ```
    *   **`rpi-rgb-led-matrix`:** ( **Required for actual hardware output** ) Henner Zeller's library for controlling RGB LED matrices with Raspberry Pi. Installation can be complex and involves compiling C++ code. Follow the instructions carefully: https://github.com/hzeller/rpi-rgb-led-matrix

## Project Code Structure

*   `main.py`: Contains the main game loop, handles user input, updates game state, and manages drawing. Initializes game elements.
*   `objects.py`: Defines the core game classes:
    *   `Timer`: A simple class to manage time-based events (like movement speed).
    *   `Pixel`: Represents a single pixel on the display grid (currently draws using `pygame`).
    *   `Game_Element`: Represents movable objects like the ball and paddle, handling their position, dimensions, color, movement logic, and drawing by updating `Pixel` colors.
*   `time.py`: Contains a `Timer` class identical to the one in `objects.py`. (Note: This is redundant and could be cleaned up).

## Installation & Setup

1.  **Set up Raspberry Pi:** Install Raspberry Pi OS and configure basic settings (network, etc.).
2.  **Connect Hardware:**
    *   Carefully connect the RGB Matrix HAT to the Raspberry Pi's GPIO pins.
    *   Connect the LED Matrix panel to the HAT using the ribbon cable. Pay attention to the input/output ports and orientation.
    *   Connect the dedicated power supply to the HAT's power input terminals. **Do not** try to power the matrix solely from the Pi's USB port or GPIO pins.
    *   Connect the keyboard to the Raspberry Pi.
3.  **Install Software Dependencies:**
    *   Open a terminal on the Raspberry Pi.
    *   Install `pygame`: `pip install pygame`
    *   Install the `rpi-rgb-led-matrix` library following its specific instructions (this often requires cloning the repository, potentially running installation scripts, and may require `sudo` privileges).
4.  **Clone this Repository:**
    ```bash
    git clone https://github.com/aidanschneider17/kiddiekarnival/
    cd kiddiekarnival
    ```

## How to Run (Current Simulation)

The current code runs a simulation in a Pygame window:

1.  Navigate to the source directory:
    ```bash
    cd src
    ```
2.  Run the main script:
    ```bash
    python main.py
    ```
3.  A Pygame window should appear displaying the game grid, paddle, and ball.

## Controls

*   **UP Arrow Key:** Move the blue paddle up.
*   **DOWN Arrow Key:** Move the blue paddle down.
*   **Close Window / CTRL+C:** Quit the game.

## Adapting for LED Matrix Hardware (Required Next Steps)

The current code in `main.py` and `objects.py` uses `pygame.draw.rect` within the `Pixel.draw` method and `draw_window` function to display the game in a desktop window. To run this on the actual 64x64 LED Matrix, significant modifications are needed:

1.  **Import `rpi-rgb-led-matrix`:** Add `from rgbmatrix import RGBMatrix, RGBMatrixOptions` to `main.py`.
2.  **Configure Matrix Options:** Set up `RGBMatrixOptions` according to your specific hardware (matrix dimensions, GPIO mapping, hardware type, brightness, etc.). Refer to the `rpi-rgb-led-matrix` library documentation.
3.  **Initialize Matrix:** Create an `RGBMatrix` instance using the configured options.
4.  **Replace Drawing Logic:**
    *   Remove the `pygame.display.set_mode`, `Pixel.draw`, and `draw_window` functions (or repurpose `draw_window`).
    *   Instead of drawing Pygame rectangles, use the `matrix.SetPixel(x, y, r, g, b)` method from the `rpi-rgb-led-matrix` library.
    *   The main loop should iterate through the `pixels` grid (defined in `main.py`) and call `matrix.SetPixel` for each pixel based on its `_color` attribute.
    *   Drawing needs to be done onto an offscreen canvas provided by the library (`matrix.CreateFrameCanvas()`) and then swapped to the display (`matrix.SwapOnVSync(canvas)`) for smooth animation.
5.  **Run with `sudo`:** Scripts using the `rpi-rgb-led-matrix` library typically require `sudo` privileges to access hardware: `sudo python main.py`.

## Future Improvements / Known Issues

*   **Hardware Integration:** The primary next step is integrating the `rpi-rgb-led-matrix` library as described above.
*   **Scoring:** Implement a scoring system.
*   **Game Over/Win Condition:** Add conditions for ending the game (e.g., ball goes past the paddle).
*   **Difficulty:** Implement increasing ball speed over time.
*   **Sound:** Add simple sound effects for bounces.
*   **Start Screen/Menu:** Add a basic menu or start screen.
