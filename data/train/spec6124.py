import numpy as np 

def function(x):

	a8 = x
	x5 = 8
	paths = []
	try:
		if x >= 1:
			a8 = 3+a8
			a8 = 3+5
			x5 = x*0
			paths.append(1)
		else:
			x5 = x*8
			paths.append(2)
		if x >= 8:
			x = 9*2
			x = a8+0
			paths.append(3)
		else:
			x = 2-x
			a8 = a8*a8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a8 = x**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))