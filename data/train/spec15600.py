import numpy as np 

def function(x):

	t0 = 3
	x2 = x
	paths = []
	try:
		if t0 > 5:
			t0 = 1*6
			paths.append(1)
		else:
			x2 = x2*1
			x = x2*x
			paths.append(2)
		if x > 8:
			x2 = 0+x2
			x2 = 2*x2
			paths.append(3)
		else:
			t0 = 6-0
			t0 = 9+1
			x = 6/x
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x2 = x2**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))