import numpy as np 

def function(x):

	j0 = 5
	r1 = x
	paths = []
	try:
		if x > 6:
			r1 = 3+x
			paths.append(1)
		else:
			j0 = j0-8
			paths.append(2)
		if x <= 2:
			r1 = j0/2
			j0 = 3+r1
			x = 8*x
			paths.append(3)
		else:
			x = x*x
			x = x/j0
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		x = j0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))