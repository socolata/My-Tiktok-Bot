# -*- coding: utf-8 -*-
"""
TIKBOT - Zefoy Automator PRO (REPOSTS UPDATE)
Created by @socolata | © 2026
Version: 4.2.0 (Obfuscated & Reposts Included)
"""

import os
import time
import sys
import base64
from datetime import datetime
from colorama import Fore, init, Style

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager

init(autoreset=True)

class TikBotSecureV2:
    def __init__(self):
        self.options = Options()
        self.options.add_argument("--disable-notifications")
        self.options.add_argument("--log-level=3")
        self.options.add_experimental_option('excludeSwitches', ['enable-logging', 'enable-automation'])
        
        self.base_url = "https://zefoy.com/"
        self.discord_url = "https://discord.gg/JK3aCFbHce" 
        
        # --- SECURE DATA STORAGE (Base64) ---
        # Added Reposts to all arrays (8th element)
        self._raw_data = {
            'services': [
                "L2h0bWwvYm9keS9kaXZbNl0vZGl2L2RpdlsyXS9kaXYvZGl2L2RpdlsyXS9kaXYvYnV0dG9u", # Followers
                "L2h0bWwvYm9keS9kaXZbNl0vZGl2L2RpdlsyXS9kaXYvZGl2L2RpdlszXS9kaXYvYnV0dG9u", # Hearts
                "L2h0bWwvYm9keS9kaXZbNl0vZGl2L2RpdlsyXS9kaXYvZGl2L2Rpdls0XS9kaXYvYnV0dG9u", # Comm Hearts
                "L2h0bWwvYm9keS9kaXZbNl0vZGl2L2RpdlsyXS9kaXYvZGl2L2Rpdls1XS9kaXYvYnV0dG9u", # Views
                "L2h0bWwvYm9keS9kaXZbNl0vZGl2L2RpdlsyXS9kaXYvZGl2L2Rpdls2XS9kaXYvYnV0dG9u", # Shares
                "L2h0bWwvYm9keS9kaXZbNl0vZGl2L2RpdlsyXS9kaXYvZGl2L2Rpdls3XS9kaXYvYnV0dG9u", # Favorites
                "L2h0bWwvYm9keS9kaXZbNl0vZGl2L2RpdlsyXS9kaXYvZGl2L2Rpdls4XS9kaXYvYnV0dG9u", # Livestream
                "L2h0bWwvYm9keS9kaXZbNl0vZGl2L2RpdlsyXS9kaXYvZGl2L2Rpdls5XS9kaXYvYnV0dG9u"  # REPOSTS (NEW)
            ],
            'inputs': [
                "L2h0bWwvYm9keS9kaXZbN10vZGl2L2Zvcm0vZGl2L2lucHV0", "L2h0bWwvYm9keS9kaXZbOF0vZGl2L2Zvcm0vZGl2L2lucHV0",
                "L2h0bWwvYm9keS9kaXZbOV0vZGl2L2Zvcm0vZGl2L2lucHV0", "L2h0bWwvYm9keS9kaXZbMTBdL2Rpdi9mb3JtL2Rpdi9pbnB1dA==",
                "L2h0bWwvYm9keS9kaXZbMTFdL2Rpdi9mb3JtL2Rpdi9pbnB1dA==", "L2h0bWwvYm9keS9kaXZbMTJdL2Rpdi9mb3JtL2Rpdi9pbnB1dA==",
                "L2h0bWwvYm9keS9kaXZbMTNdL2Rpdi9mb3JtL2Rpdi9pbnB1dA==", "L2h0bWwvYm9keS9kaXZbMTRdL2Rpdi9mb3JtL2Rpdi9pbnB1dA=="
            ],
            'search': [
                "L2h0bWwvYm9keS9kaXZbN10vZGl2L2Zvcm0vZGl2L2Rpdi9idXR0b24=", "L2h0bWwvYm9keS9kaXZbOF0vZGl2L2Zvcm0vZGl2L2Rpdi9idXR0b24=",
                "L2h0bWwvYm9keS9kaXZbOV0vZGl2L2Zvcm0vZGl2L2Rpdi9idXR0b24=", "L2h0bWwvYm9keS9kaXZbMTBdL2Rpdi9mb3JtL2Rpdi9kaXYvYnV0dG9u",
                "L2h0bWwvYm9keS9kaXZbMTFdL2Rpdi9mb3JtL2Rpdi9kaXYvYnV0dG9u", "L2h0bWwvYm9keS9kaXZbMTJdL2Rpdi9mb3JtL2Rpdi9kaXYvYnV0dG9u",
                "L2h0bWwvYm9keS9kaXZbMTNdL2Rpdi9mb3JtL2Rpdi9kaXYvYnV0dG9u", "L2h0bWwvYm9keS9kaXZbMTRdL2Rpdi9mb3JtL2Rpdi9kaXYvYnV0dG9u"
            ],
            'send': [
                "L2h0bWwvYm9keS9kaXZbN10vZGl2L2Rpdi9kaXZbMV0vZGl2L2Zvcm0vYnV0dG9u", "L2h0bWwvYm9keS9kaXZbOF0vZGl2L2Rpdi9kaXZbMV0vZGl2L2Zvcm0vYnV0dG9u",
                "L2h0bWwvYm9keS9kaXZbOV0vZGl2L2Rpdi9kaXZbMV0vZGl2L2Zvcm0vYnV0dG9u", "L2h0bWwvYm9keS9kaXZbMTBdL2Rpdi9kaXYvZGl2WzFdL2Rpdi9mb3JtL2J1dHRvbg==",
                "L2h0bWwvYm9keS9kaXZbMTFdL2Rpdi9kaXYvZGl2WzFdL2Rpdi9mb3JtL2J1dHRvbg==", "L2h0bWwvYm9keS9kaXZbMTJdL2Rpdi9kaXYvZGl2WzFdL2Rpdi9mb3JtL2J1dHRvbg==",
                "L2h0bWwvYm9keS9kaXZbMTNdL2Rpdi9kaXYvZGl2WzFdL2Rpdi9mb3JtL2J1dHRvbg==", "L2h0bWwvYm9keS9kaXZbMTRdL2Rpdi9kaXYvZGl2WzFdL2Rpdi9mb3JtL2J1dHRvbg=="
            ],
            'timer': [
                "L2h0bWwvYm9keS9kaXZbN10vZGl2L2Rpdi9zcGFu", "L2h0bWwvYm9keS9kaXZbOF0vZGl2L2Rpdi9zcGFu",
                "L2h0bWwvYm9keS9kaXZbOV0vZGl2L2Rpdi9zcGFu", "L2h0bWwvYm9keS9kaXZbMTBdL2Rpdi9kaXYvc3Bhbg==",
                "L2h0bWwvYm9keS9kaXZbMTFdL2Rpdi9kaXYvc3Bhbg==", "L2h0bWwvYm9keS9kaXZbMTJdL2Rpdi9kaXYvc3Bhbg==",
                "L2h0bWwvYm9keS9kaXZbMTNdL2Rpdi9kaXYvc3Bhbg==", "L2h0bWwvYm9keS9kaXZbMTRdL2Rpdi9kaXYvc3Bhbg=="
            ]
        }

        self.xpaths = {k: [base64.b64decode(x).decode('utf-8') for x in v] for k, v in self._raw_data.items()}
        self.xpathnames = ["Followers", "Hearts", "Comment Hearts", "Views", "Shares", "Favorites", "Livestream", "Reposts"]
        self.video_url = ""
        self.option = 0

        self.log("Initializing TikBot Engine v4.2...", "info")
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=self.options)

    def log(self, message, type="info"):
        t = datetime.now().strftime("%H:%M:%S")
        colors = {"info": Fore.CYAN, "success": Fore.GREEN, "error": Fore.RED, "warning": Fore.YELLOW}
        print(f"[{t}] {colors.get(type, Fore.WHITE)}[{type.upper()}] {message}")

    def print_banner(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.GREEN + Style.BRIGHT + """
  _______ _____ _  _______  ____ _______ 
 |__   __|_   _| |/ /  _  |/ __ \__   __|
    | |    | | | ' /| |_) | |  | | | |   
    | |    | | |  < |  _ <| |  | | | |   
    | |   _| |_| . \| |_) | |__| | | |   
    |_|  |_____|_|\_\____/ \____/  |_|   
                                         
          [ CREATED BY @SOCOLATA ]
          [  REPOSTS UPDATED 2026 ]
        """ + Fore.RESET)

    def solve_captcha(self):
        self.log("Solve the CAPTCHA in Chrome...", "warning")
        while True:
            try:
                if self.driver.find_elements(By.CLASS_NAME, 'row'):
                    self.log("CAPTCHA Passed!", "success")
                    break
                time.sleep(2)
            except: pass

    def menu(self):
        print(f"\n{Fore.YELLOW}>> SELECT SERVICE [1-9]:{Fore.RESET}")
        for i, name in enumerate(self.xpathnames):
            try:
                element = self.driver.find_element(By.XPATH, self.xpaths['services'][i])
                status = f"{Fore.GREEN}[ONLINE]" if element.is_enabled() else f"{Fore.RED}[OFFLINE]"
            except: status = f"{Fore.RED}[LOCKED]"
            print(f" [{i+1}] {name.ljust(15)} {status}")
        print(f" [9] Support Discord {Fore.MAGENTA}[COMMUNITY]\n")

    def select(self):
        while True:
            try:
                self.option = int(input(f"{Fore.WHITE}Choice: "))
                if self.option == 9:
                    self.driver.get(self.discord_url)
                    sys.exit()
                if 1 <= self.option <= 8: break
            except: pass
        self.driver.find_element(By.XPATH, self.xpaths['services'][self.option-1]).click()

    def inject_link(self):
        if not self.video_url:
            print(f"\n{Fore.CYAN}>> TikTok Link:")
            self.video_url = input(f"{Fore.WHITE}> ")
        try:
            field = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, self.xpaths['inputs'][self.option-1]))
            )
            field.clear()
            field.send_keys(self.video_url)
        except:
            self.log("Critical Error: Link field hidden", "error")
            sys.exit()

    def run_bot(self):
        self.log(f"Auto-Loop started for {self.xpathnames[self.option-1]}", "success")
        while True:
            try:
                WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, self.xpaths['search'][self.option-1]))
                ).click()
                time.sleep(3)

                try:
                    self.driver.find_element(By.XPATH, self.xpaths['send'][self.option-1]).click()
                    self.log(f"Sent {self.xpathnames[self.option-1]}!", "success")
                    time.sleep(5)
                except:
                    try:
                        timer_val = self.driver.find_element(By.XPATH, self.xpaths['timer'][self.option-1]).text
                        self.log(f"Waiting for timer: {timer_val}", "warning")
                        WebDriverWait(self.driver, 1200).until(
                            lambda d: "READY" in d.find_element(By.XPATH, self.xpaths['timer'][self.option-1]).text
                        )
                    except: pass
            except:
                self.driver.refresh()
                time.sleep(5)
                self.inject_link()

    def start(self):
        try:
            self.print_banner()
            self.driver.get(self.base_url)
            self.solve_captcha()
            self.menu()
            self.select()
            self.inject_link()
            self.run_bot()
        except KeyboardInterrupt:
            self.log("User Exit.", "warning")
        finally:
            self.driver.quit()

if __name__ == "__main__":
    TikBotSecureV2().start()