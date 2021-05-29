import numpy as np 

def function(x):

	k1 = x
	t7 = 0
	paths = []
	try:
		if x >= 3:
			k1 = k1+8
			paths.append(1)
		else:
			t7 = t7+4
			paths.append(2)
		if x < 4:
			t7 = t7/5
			paths.append(3)
		else:
			k1 = 2*5
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