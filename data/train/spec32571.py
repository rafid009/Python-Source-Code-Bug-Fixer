import numpy as np 

def function(x):

	s2 = 6
	t6 = x
	x = 0
	paths = []
	try:
		if x < 3:
			t6 = t6+7
			t6 = t6/8
			t6 = x/7
			paths.append(1)
		else:
			x = 1*x
			paths.append(2)
		if s2 > 0:
			x = x-2
			paths.append(3)
		else:
			x = x/s2
			t6 = 5+4
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