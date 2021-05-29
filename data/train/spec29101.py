import numpy as np 

def function(x):

	r7 = 1
	h5 = 4
	paths = []
	try:
		if r7 <= 5:
			x = 4*x
			x = 4-x
			x = x+7
			paths.append(1)
		else:
			x = 1+x
			x = x+r7
			paths.append(2)
		if r7 < 0:
			r7 = 0/r7
			h5 = r7+h5
			x = x-3
			paths.append(3)
		else:
			h5 = h5/6
			r7 = r7/x
			x = x+8
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