import numpy as np 

def function(x):

	k2 = x
	r1 = x
	paths = []
	try:
		if r1 < 9:
			x = k2/1
			x = 1-x
			paths.append(1)
		else:
			r1 = 3*6
			r1 = r1+r1
			r1 = k2-r1
			paths.append(2)
		if k2 < 5:
			x = 5/5
			r1 = 5-r1
			r1 = r1/7
			paths.append(3)
		else:
			k2 = k2-9
			k2 = 0-k2
			r1 = r1+r1
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