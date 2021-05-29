import numpy as np 

def function(x):

	v7 = 0
	r5 = x
	paths = []
	try:
		if r5 <= 3:
			r5 = x/r5
			x = v7+x
			paths.append(1)
		else:
			r5 = 3+r5
			x = 0+x
			x = x/2
			paths.append(2)
		if x >= 3:
			r5 = 5*r5
			paths.append(3)
		else:
			x = x/6
			v7 = 2-3
			v7 = v7-v7
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