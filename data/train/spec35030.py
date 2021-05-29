import numpy as np 

def function(x):

	n9 = 3
	t6 = 8
	x = 2
	paths = []
	try:
		if n9 <= 7:
			t6 = 3+t6
			paths.append(1)
		else:
			t6 = t6-6
			x = x*1
			paths.append(2)
		if t6 < 0:
			x = 9+1
			paths.append(3)
		else:
			x = t6*6
			x = 1-x
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