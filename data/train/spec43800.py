import numpy as np 

def function(x):

	r7 = x
	x0 = 2
	paths = []
	try:
		if r7 < 0:
			x0 = x0*3
			r7 = 9+r7
			paths.append(1)
		else:
			r7 = x/r7
			x0 = 0-5
			r7 = r7*5
			paths.append(2)
		if x >= 1:
			x = x*8
			x0 = x0+8
			r7 = x/8
			paths.append(3)
		else:
			x0 = 7/r7
			x0 = 7/x0
			r7 = 6+r7
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		x = r7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))