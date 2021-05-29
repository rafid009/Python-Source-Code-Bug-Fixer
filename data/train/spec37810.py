import numpy as np 

def function(x):

	y2 = 9
	f4 = 9
	paths = []
	try:
		if x <= 1:
			x = f4+x
			x = x+x
			paths.append(1)
		else:
			x = 8*x
			paths.append(2)
		if y2 >= 8:
			f4 = 4/2
			y2 = 4*y2
			f4 = 4-6
			paths.append(3)
		else:
			x = f4/8
			paths.append(4)
		paths.append(5)
		assert f4 >= 0
		x = f4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))