import numpy as np 

def function(x):

	a5 = 1
	v3 = x
	paths = []
	try:
		if a5 > 2:
			a5 = 8+x
			a5 = a5+1
			a5 = 6/a5
			paths.append(1)
		else:
			x = 2/v3
			a5 = 8/a5
			a5 = a5*a5
			paths.append(2)
		if v3 <= 7:
			v3 = a5-a5
			x = a5*x
			x = x-8
			paths.append(3)
		else:
			v3 = v3-0
			x = 4*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a5 = x**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))