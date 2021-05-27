import numpy as np 

def function(x):

	k6 = x
	e2 = 2
	paths = []
	try:
		if x < 0:
			k6 = 1+k6
			x = x*e2
			paths.append(1)
		else:
			x = x*x
			k6 = 8+k6
			paths.append(2)
		if x >= 4:
			x = x*6
			k6 = k6/3
			paths.append(3)
		else:
			e2 = k6+x
			x = x/x
			paths.append(4)
		paths.append(5)
		assert e2 >= 0
		x = e2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))