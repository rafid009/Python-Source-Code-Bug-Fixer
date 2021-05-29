import numpy as np 

def function(x):

	t1 = x
	k7 = x
	paths = []
	try:
		if k7 > 1:
			x = x/k7
			t1 = 3*t1
			paths.append(1)
		else:
			t1 = t1*4
			paths.append(2)
		if t1 < 0:
			t1 = t1*k7
			paths.append(3)
		else:
			k7 = 3/t1
			k7 = 2-k7
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