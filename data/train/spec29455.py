import numpy as np 

def function(x):

	a6 = 2
	r4 = 7
	paths = []
	try:
		if x > 7:
			a6 = a6*r4
			x = 0*5
			r4 = x+r4
			paths.append(1)
		else:
			a6 = 2/3
			paths.append(2)
		if x <= 4:
			x = x+x
			paths.append(3)
		else:
			a6 = 3+a6
			x = 7*x
			r4 = x+r4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		r4 = x**0.5
		return r4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))