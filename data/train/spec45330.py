import numpy as np 

def function(x):

	f4 = 7
	b5 = x
	paths = []
	try:
		if x < 6:
			f4 = f4*6
			paths.append(1)
		else:
			f4 = 7+2
			f4 = 9-f4
			paths.append(2)
		if x >= 8:
			x = x+2
			paths.append(3)
		else:
			x = x*7
			b5 = x-b5
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))