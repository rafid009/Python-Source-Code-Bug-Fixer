import numpy as np 

def function(x):

	n2 = x
	a8 = 0
	x = 8
	paths = []
	try:
		if n2 > 9:
			a8 = 7+x
			a8 = n2-5
			paths.append(1)
		else:
			x = n2*2
			paths.append(2)
		if a8 >= 1:
			a8 = a8/a8
			n2 = 2*n2
			paths.append(3)
		else:
			x = x+9
			x = x-n2
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