import numpy as np 

def function(x):

	f4 = x
	n8 = 6
	paths = []
	try:
		if n8 <= 8:
			f4 = n8*6
			paths.append(1)
		else:
			f4 = 2+n8
			paths.append(2)
		if f4 > 2:
			f4 = f4-f4
			x = x-4
			x = x+9
			paths.append(3)
		else:
			x = 4-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))