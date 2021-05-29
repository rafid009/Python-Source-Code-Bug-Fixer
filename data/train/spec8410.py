import numpy as np 

def function(x):

	o9 = 3
	l8 = x
	x = x
	paths = []
	try:
		if o9 > 4:
			x = x+1
			paths.append(1)
		else:
			o9 = o9+7
			paths.append(2)
		if x <= 7:
			o9 = 5+l8
			o9 = 5*6
			l8 = 9*l8
			paths.append(3)
		else:
			x = x/1
			l8 = o9*l8
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