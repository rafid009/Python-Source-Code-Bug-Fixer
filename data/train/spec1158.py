import numpy as np 

def function(x):

	q1 = 6
	v0 = 4
	paths = []
	try:
		if v0 < 7:
			v0 = 2/v0
			q1 = q1-2
			v0 = 5/4
			paths.append(1)
		else:
			v0 = v0/x
			x = x/8
			v0 = 8*v0
			paths.append(2)
		if x <= 3:
			x = 8+x
			paths.append(3)
		else:
			q1 = q1/x
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))