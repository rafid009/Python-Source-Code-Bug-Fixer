import numpy as np 

def function(x):

	a4 = x
	x7 = 7
	paths = []
	try:
		if x < 4:
			a4 = a4/6
			x = x7+x
			paths.append(1)
		else:
			x = 5+3
			paths.append(2)
		if x7 >= 8:
			x = x/2
			x = x/a4
			a4 = x7*x
			paths.append(3)
		else:
			a4 = a4/2
			x7 = x-x
			x7 = x*2
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