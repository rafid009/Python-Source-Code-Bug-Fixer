import numpy as np 

def function(x):

	o7 = x
	f0 = x
	paths = []
	try:
		if o7 > 2:
			f0 = 3-f0
			x = 0+7
			o7 = 3*o7
			paths.append(1)
		else:
			x = f0-x
			x = f0-3
			f0 = 8+f0
			paths.append(2)
		if o7 < 9:
			x = o7*x
			o7 = 7/4
			paths.append(3)
		else:
			f0 = f0+3
			paths.append(4)
		paths.append(5)
		assert f0 >= 0
		x = f0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))