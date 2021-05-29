import numpy as np 

def function(x):

	i1 = 7
	a8 = 1
	paths = []
	try:
		if a8 >= 7:
			a8 = 0/a8
			x = x+2
			a8 = x*x
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if a8 < 3:
			x = i1/x
			i1 = 0/i1
			a8 = 6/7
			paths.append(3)
		else:
			i1 = i1*5
			i1 = 4*i1
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