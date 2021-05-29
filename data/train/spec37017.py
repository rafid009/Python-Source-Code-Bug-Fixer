import numpy as np 

def function(x):

	f0 = 0
	i2 = 4
	paths = []
	try:
		if f0 > 2:
			f0 = f0*3
			f0 = 7+f0
			paths.append(1)
		else:
			i2 = 8+i2
			paths.append(2)
		if f0 <= 3:
			f0 = f0*4
			paths.append(3)
		else:
			x = x/4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f0 = x**0.5
		return f0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))