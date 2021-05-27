import numpy as np 

def function(x):

	j0 = x
	r1 = x
	paths = []
	try:
		if r1 <= 4:
			r1 = x*r1
			paths.append(1)
		else:
			j0 = x/j0
			j0 = j0/7
			x = x*9
			paths.append(2)
		if x > 6:
			r1 = 5+0
			x = j0-x
			r1 = r1-1
			paths.append(3)
		else:
			j0 = 8+r1
			x = 2*x
			r1 = 9-8
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