#!/usr/bin/env python3.9

from person import Person

def main():
	f = Person(5)
	print(f.get())
	f.set(7)
	print(f"kan man få en fibbe eller?: {f.fib()}")
	print(f.get())
	

if __name__ == '__main__':
	main()
