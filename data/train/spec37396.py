import numpy as np 

def function(x):

	t3 = 8
	k1 = x
	paths = []
	try:
		if t3 <= 0:
			k1 = k1+5
			paths.append(1)
		else:
			k1 = 6*k1
			t3 = 0/3
			paths.append(2)
		if t3 < 2:
			k1 = 6-k1
			k1 = 1/4
			paths.append(3)
		else:
			k1 = 6-3
			x = x/x
			t3 = k1*7
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