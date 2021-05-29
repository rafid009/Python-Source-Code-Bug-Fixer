import numpy as np 

def function(x):

	o4 = 2
	a3 = x
	paths = []
	try:
		if a3 <= 4:
			a3 = a3-a3
			paths.append(1)
		else:
			o4 = a3/x
			o4 = x+x
			paths.append(2)
		if o4 >= 8:
			x = a3/8
			x = 2/x
			x = x*7
			paths.append(3)
		else:
			o4 = 9/o4
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