import numpy as np 

def function(x):

	x6 = x
	t0 = x
	paths = []
	try:
		if x6 > 7:
			x6 = x6*7
			t0 = 5+5
			paths.append(1)
		else:
			x6 = 0+x6
			paths.append(2)
		if x < 2:
			x = x-6
			t0 = 1+t0
			paths.append(3)
		else:
			x6 = 0-x
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x6 = x6**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))