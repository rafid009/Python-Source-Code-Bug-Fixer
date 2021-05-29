import numpy as np 

def function(x):

	f9 = x
	b3 = 5
	paths = []
	try:
		if x > 6:
			x = x+6
			x = x/f9
			b3 = 3/b3
			paths.append(1)
		else:
			x = x-7
			paths.append(2)
		if x >= 1:
			b3 = b3*9
			paths.append(3)
		else:
			f9 = 7-1
			f9 = b3/f9
			f9 = b3/f9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))