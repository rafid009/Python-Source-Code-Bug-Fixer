import numpy as np 

def function(x):

	t6 = x
	x0 = 7
	paths = []
	try:
		if x >= 0:
			x = x-t6
			paths.append(1)
		else:
			x0 = t6+x0
			paths.append(2)
		if t6 > 3:
			x0 = 1*x0
			paths.append(3)
		else:
			t6 = x0*1
			x0 = x0*6
			paths.append(4)
		paths.append(5)
		assert x0 >= 0
		x0 = x0**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))