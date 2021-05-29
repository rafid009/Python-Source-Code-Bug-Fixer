import numpy as np 

def function(x):

	f9 = 6
	j6 = x
	paths = []
	try:
		if f9 < 2:
			f9 = f9+j6
			x = j6/1
			x = x-6
			paths.append(1)
		else:
			j6 = 5*9
			f9 = f9*x
			paths.append(2)
		if f9 <= 4:
			f9 = 1*f9
			f9 = 4/f9
			x = x+f9
			paths.append(3)
		else:
			f9 = 2/j6
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