import numpy as np 

def function(x):

	r4 = x
	x1 = x
	paths = []
	try:
		if r4 <= 5:
			x1 = x1-6
			paths.append(1)
		else:
			r4 = x/r4
			paths.append(2)
		if r4 >= 5:
			r4 = x1-0
			paths.append(3)
		else:
			x1 = x+x1
			x = 1+x
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		x = r4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))