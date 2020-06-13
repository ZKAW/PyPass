# PyPass
This is a random password generator in python that does NOT store ANY of your data.

**Where can I use it ?:**

- Windows (.exe compiled version available on [GitHub](https://github.com/ZKAW/Py-Pass))
- Ubuntu
- macOS

**With this script, you can:**

- Select the password length
- Enable/disable numbers
- Enable/disable special chars
- Change the special char list

**HOW TO DOWNLOAD:**

* `pip3 install py_pass`
<br/> or <br/>
* `git clone https://github.com/ZKAW/PyPass`
<br/> or <br/>
* Download the .zip [by clicking here](https://github.com/ZKAW/Py-Pass/archive/master.zip)


**HOW TO LAUNCH:**

* Import the script with: `from py_pass import randPass`
<br/> or <br/> 
* Launch the script with: `python3 PyPass.py` (python3 required)
<br/> or <br/>
* Launch the Windows .exe (python not required)

**HOW TO USE PIP MODULE:**

- `from py_pass import randPass`
- `print(randPass())`

randPass can take four arguments:

- stringLength -> Password length, in integer (default=12).
- isNumber -> Is the password should include numbers, in boolean (default=True).
- isSpecial -> Is the password should include special characters, in boolean (default=True).
- specialChars -> The special characters ASCII map, in string (default=specials).

**HOW TO HELP ME:**

- Like
- Fork
- Tell your friend about it ! :)

**⚠ DISCLAIMER 	⚠**

This script is not storing ANY of your data, so you can use it in a totally transparent and safe way. Enjoy ! :)
