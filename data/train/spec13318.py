import numpy as np 

def function(x):

	t6 = x
	x6 = x
	paths = []
	try:
		if x6 >= 8:
			x = 3+x6
			t6 = 7*x6
			paths.append(1)
		else:
			x = 4*x
			x6 = t6*6
			paths.append(2)
		if x < 8:
			x = x*7
			t6 = 0*t6
			x = 6-6
			paths.append(3)
		else:
			x6 = x6/t6
			x6 = 3/x
			paths.append(4)
		paths.append(5)
		assert x6 >= 0
		x = x6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))