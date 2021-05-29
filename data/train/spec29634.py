import numpy as np 

def function(x):

	i2 = 0
	f4 = 5
	paths = []
	try:
		if f4 >= 5:
			i2 = f4/7
			paths.append(1)
		else:
			i2 = x-f4
			paths.append(2)
		if x < 6:
			f4 = 1-1
			f4 = f4*4
			paths.append(3)
		else:
			x = x+4
			f4 = 3*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))