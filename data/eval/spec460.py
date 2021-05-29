import numpy as np 

def function(x):

	v2 = x
	q2 = 2
	paths = []
	try:
		if x < 9:
			q2 = 8-x
			paths.append(1)
		else:
			q2 = q2/8
			x = 9*x
			x = 8+x
			paths.append(2)
		if v2 > 4:
			x = v2*7
			x = x+2
			paths.append(3)
		else:
			v2 = 6/v2
			v2 = 8*v2
			q2 = 2-q2
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