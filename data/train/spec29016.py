import numpy as np 

def function(x):

	r6 = 8
	v6 = 6
	paths = []
	try:
		if x >= 0:
			r6 = r6*r6
			r6 = 9*x
			x = 4/x
			paths.append(1)
		else:
			x = 5+6
			paths.append(2)
		if x >= 6:
			r6 = 2-3
			paths.append(3)
		else:
			x = x/3
			r6 = r6/4
			r6 = r6/v6
			paths.append(4)
		paths.append(5)
		assert r6 >= 0
		v6 = r6**0.5
		return v6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))