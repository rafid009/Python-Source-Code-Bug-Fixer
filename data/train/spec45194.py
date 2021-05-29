import numpy as np 

def function(x):

	y0 = x
	t4 = 0
	paths = []
	try:
		if x >= 5:
			x = x-2
			x = 6-x
			paths.append(1)
		else:
			y0 = t4+y0
			paths.append(2)
		if t4 > 9:
			y0 = 9+y0
			y0 = 2*0
			paths.append(3)
		else:
			t4 = t4/8
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))