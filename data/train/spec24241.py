import numpy as np 

def function(x):

	v4 = x
	r4 = x
	paths = []
	try:
		if v4 < 2:
			v4 = 3+x
			paths.append(1)
		else:
			r4 = r4*8
			x = 0*6
			paths.append(2)
		if v4 < 1:
			x = 4/x
			x = x-3
			paths.append(3)
		else:
			r4 = 1-r4
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		x = v4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))