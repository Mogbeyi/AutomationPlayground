#!/usr/bin/python3
# pw.py - An insecure password locker program.
import sys, pyperclip

# These are pseudo passwords
PASSWORDS = {
	'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
	'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
	'luggage': '12345'
}

if len(sys.argv) < 2:
	print('Usage: python pw.py [account] - copy account password')
	sys.exit()

account = sys.argv[1].lower()
password = PASSWORDS.get(account, False)

if password:
	pyperclip.copy(PASSWORDS[account])
	print(f'Password for {account} copied to clipboard.')
else:
	print(f"There is no account named {account}")

