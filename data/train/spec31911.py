import numpy as np 

def function(x):

	y6 = x
	t8 = x
	paths = []
	try:
		if y6 > 0:
			t8 = 5-t8
			y6 = y6/4
			paths.append(1)
		else:
			t8 = 5-7
			paths.append(2)
		if x > 0:
			x = y6+x
			y6 = 0*y6
			t8 = t8+6
			paths.append(3)
		else:
			t8 = t8-y6
			t8 = t8-6
			t8 = 8-t8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y6 = x**0.5
		return y6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))