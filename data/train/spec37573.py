import numpy as np 

def function(x):

	t7 = x
	z7 = 1
	paths = []
	try:
		if z7 > 2:
			t7 = 4*x
			t7 = 8*t7
			t7 = t7-5
			paths.append(1)
		else:
			x = 1+x
			paths.append(2)
		if x > 0:
			t7 = t7*2
			x = x/2
			paths.append(3)
		else:
			t7 = 0/z7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		z7 = x**0.5
		return z7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))