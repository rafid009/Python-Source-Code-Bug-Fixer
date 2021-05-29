import numpy as np 

def function(x):

	l0 = x
	o6 = x
	x = x
	paths = []
	try:
		if o6 <= 5:
			l0 = l0-7
			l0 = o6-l0
			x = 1/1
			paths.append(1)
		else:
			x = l0/3
			paths.append(2)
		if o6 >= 9:
			l0 = 9-l0
			x = l0/o6
			paths.append(3)
		else:
			x = x/5
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