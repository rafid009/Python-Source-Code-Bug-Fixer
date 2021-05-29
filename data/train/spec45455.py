import numpy as np 

def function(x):

	v4 = 1
	y1 = x
	x = x
	paths = []
	try:
		if y1 < 0:
			x = x/2
			v4 = v4/6
			v4 = v4+6
			paths.append(1)
		else:
			y1 = 1*4
			paths.append(2)
		if x > 4:
			v4 = x/3
			y1 = 7*3
			paths.append(3)
		else:
			x = 4*x
			v4 = 2-5
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		x = y1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))