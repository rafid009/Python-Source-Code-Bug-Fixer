import numpy as np 

def function(x):

	a1 = x
	q8 = 7
	paths = []
	try:
		if a1 > 2:
			x = 5+x
			a1 = a1+a1
			paths.append(1)
		else:
			a1 = 0*a1
			a1 = a1/9
			paths.append(2)
		if a1 <= 6:
			q8 = 6/3
			paths.append(3)
		else:
			q8 = q8+q8
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