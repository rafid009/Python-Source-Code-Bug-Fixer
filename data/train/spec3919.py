import numpy as np 

def function(x):

	v0 = x
	q9 = x
	paths = []
	try:
		if v0 < 5:
			v0 = v0*8
			x = 6/x
			paths.append(1)
		else:
			v0 = 3/v0
			v0 = v0-2
			q9 = q9/x
			paths.append(2)
		if v0 <= 1:
			q9 = 1/q9
			paths.append(3)
		else:
			v0 = 1*v0
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