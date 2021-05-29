import numpy as np 

def function(x):

	t0 = 9
	y6 = x
	paths = []
	try:
		if x < 8:
			x = y6/9
			paths.append(1)
		else:
			y6 = t0/y6
			paths.append(2)
		if x >= 8:
			y6 = 0-y6
			t0 = t0*0
			paths.append(3)
		else:
			t0 = t0+1
			x = x+1
			paths.append(4)
		paths.append(5)
		assert y6 >= 0
		y6 = y6**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))