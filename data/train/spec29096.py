import numpy as np 

def function(x):

	t6 = x
	y8 = 1
	paths = []
	try:
		if y8 < 3:
			t6 = 9+t6
			paths.append(1)
		else:
			y8 = y8*y8
			y8 = x*0
			x = 8*x
			paths.append(2)
		if t6 < 2:
			y8 = 9+0
			paths.append(3)
		else:
			x = 5*y8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y8 = x**0.5
		return y8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))