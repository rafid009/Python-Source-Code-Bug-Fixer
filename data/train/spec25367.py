import numpy as np 

def function(x):

	f3 = x
	y4 = 0
	paths = []
	try:
		if y4 < 3:
			x = x-4
			x = 8*x
			x = y4*x
			paths.append(1)
		else:
			y4 = x-4
			x = 7/f3
			paths.append(2)
		if x > 7:
			x = 9+0
			y4 = x/6
			y4 = y4*y4
			paths.append(3)
		else:
			f3 = y4*f3
			f3 = f3-2
			y4 = y4*y4
			paths.append(4)
		paths.append(5)
		assert f3 >= 0
		x = f3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))