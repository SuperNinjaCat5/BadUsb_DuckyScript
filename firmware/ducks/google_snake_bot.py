import pyautogui
import time

DEFAULT_DELAY = 0.2  # 200 ms
SHORT_DELAY = 0.25   # 250 ms

def press_tab_n_times(n, delay=DEFAULT_DELAY):
    for _ in range(n):
        pyautogui.press('tab')
        time.sleep(delay)

def main():
    time.sleep(3)  # Give you time to switch focus

    # Press Windows key to open Start
    pyautogui.press('win')
    time.sleep(DEFAULT_DELAY)

    # Launch Microsoft Edge
    pyautogui.write('Microsoft Edge', interval=0.05)
    pyautogui.press('enter')
    time.sleep(DEFAULT_DELAY)

    # Type the Snake game URL and go to it
    pyautogui.write('https://share.google/9Ij5LWgkyi9WOUy7v', interval=0.05)
    pyautogui.press('enter')
    time.sleep(5)  # Wait for browser to load the game

    # Navigate to game
    pyautogui.press('tab')
    time.sleep(SHORT_DELAY)
    pyautogui.press('enter')
    time.sleep(DEFAULT_DELAY)

    # Tab 3 times
    press_tab_n_times(3)

    # Press Enter
    pyautogui.press('enter')
    time.sleep(0.5)

    # Tab 4 more times
    press_tab_n_times(4)

    # Final Enter to start
    pyautogui.press('enter')
    time.sleep(SHORT_DELAY)

    # Press 'd' to move snake right
    pyautogui.press('d')
    time.sleep(2.5)

if __name__ == '__main__':
    main()
