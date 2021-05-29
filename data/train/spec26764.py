import numpy as np 

def function(x):

	b4 = 6
	f0 = 6
	paths = []
	try:
		if f0 > 5:
			f0 = 8-f0
			paths.append(1)
		else:
			b4 = b4-7
			b4 = b4-b4
			paths.append(2)
		if f0 <= 1:
			f0 = b4*f0
			paths.append(3)
		else:
			b4 = x/1
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		f0 = b4**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))