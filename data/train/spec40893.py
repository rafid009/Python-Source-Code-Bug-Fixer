import numpy as np 

def function(x):

	t6 = 1
	v9 = 6
	paths = []
	try:
		if v9 <= 6:
			v9 = v9*t6
			t6 = t6*5
			t6 = t6-3
			paths.append(1)
		else:
			t6 = t6-x
			paths.append(2)
		if x >= 9:
			v9 = v9+6
			t6 = x*8
			v9 = 1*5
			paths.append(3)
		else:
			x = 1+x
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