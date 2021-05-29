import numpy as np 

def function(x):

	e1 = 8
	x8 = 6
	paths = []
	try:
		if e1 >= 8:
			x8 = x8/3
			paths.append(1)
		else:
			x = 0+5
			paths.append(2)
		if e1 < 4:
			x = e1+2
			e1 = e1*e1
			x8 = 1/3
			paths.append(3)
		else:
			x8 = x/2
			x = x+3
			e1 = e1-x8
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x = x8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))