import numpy as np 

def function(x):

	z5 = x
	r1 = 4
	paths = []
	try:
		if r1 < 3:
			r1 = 6-r1
			x = 1+3
			paths.append(1)
		else:
			x = x/6
			x = r1-5
			paths.append(2)
		if z5 >= 1:
			x = x+1
			z5 = z5/4
			paths.append(3)
		else:
			x = z5*x
			x = 9+x
			paths.append(4)
		paths.append(5)
		assert z5 >= 0
		x = z5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))