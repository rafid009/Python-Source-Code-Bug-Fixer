import numpy as np 

def function(x):

	a2 = 8
	o5 = x
	x = x
	paths = []
	try:
		if a2 < 2:
			x = 7+x
			paths.append(1)
		else:
			o5 = x+3
			a2 = 1*3
			a2 = 1-x
			paths.append(2)
		if a2 > 6:
			o5 = 0-7
			a2 = 4*3
			paths.append(3)
		else:
			x = 9-x
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))