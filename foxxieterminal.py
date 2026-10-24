import os
import subprocess
import sys
import time

print("WELCOME TO THE FOXXIE TERMINAL")


def exit_terminal():
  print("Exiting the terminal...")
  time.sleep(1)
  sys.exit()


def clear_terminal():
  os.system("cls" if os.name == "nt" else "clear")


while True:
  komut_verme = input("FOXXIE TERMINAL: ").strip()

  if komut_verme == "exit":
    exit_terminal()

  elif komut_verme == "clear":
    clear_terminal()

  elif komut_verme == "help":
    print("Available commands:")
    print("exit - Exit the terminal")
    print("clear - Clear the terminal screen")
    print("help - Show this help message")
    print("edit - edit a file")
    print("run - run a python file")
    print("pip install - install a python package")

  elif komut_verme.startswith("edit"):
    dosya_adi = komut_verme[4:].strip()
    if dosya_adi:
      with open(dosya_adi, "a", encoding="utf-8"):
        pass
      subprocess.Popen(["notepad.exe", dosya_adi])
    else:
      print("Please provide a file name to edit.")
      time.sleep(2)

  elif komut_verme == "":
    print(
        "No command entered. Type 'help' for a list of available commands.\n"
    )
    time.sleep(2)
    clear_terminal()

  elif komut_verme == "run":
    print("Usage: run <file_name.py>")
    time.sleep(2)

  elif komut_verme.startswith("run"):
    dosya_adi = komut_verme[3:].strip()
    if not dosya_adi:
      print("Please provide a file name to run.")
      time.sleep(2)
    elif not dosya_adi.endswith(".py"):
      print("Please provide a valid Python file name with .py extension.")
      time.sleep(2)
    elif not os.path.isfile(dosya_adi):
      print(f"File '{dosya_adi}' not found.")
      time.sleep(2)
    else:
      subprocess.run([sys.executable, dosya_adi])

  elif komut_verme == "Thanks":
    print(
        "This terminal was created by a71323r under the foxxie development team."
    )
    time.sleep(3)
    clear_terminal()

  elif komut_verme.startswith("pip install"):
    paket_adi = komut_verme[11:].strip()
    if not paket_adi:
      print("Please provide a package name to install.")
      time.sleep(2)
    else:
      subprocess.run([sys.executable, "-m", "pip", "install", paket_adi])

  else:
    print("Invalid command. Type 'help' for a list of available commands.\n")
    time.sleep(2)
    clear_terminal()