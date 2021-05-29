import numpy as np 

def function(x):

	a1 = x
	o5 = x
	paths = []
	try:
		if x >= 5:
			o5 = o5-4
			a1 = a1*a1
			paths.append(1)
		else:
			a1 = x/a1
			paths.append(2)
		if a1 > 0:
			x = x+x
			paths.append(3)
		else:
			x = x+9
			a1 = a1-4
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