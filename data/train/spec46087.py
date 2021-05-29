import numpy as np 

def function(x):

	t2 = x
	y4 = 4
	x = x
	paths = []
	try:
		if y4 >= 6:
			x = 0-x
			y4 = 0-y4
			y4 = y4*y4
			paths.append(1)
		else:
			t2 = 1/t2
			y4 = y4/y4
			x = x/6
			paths.append(2)
		if x < 1:
			y4 = x/6
			x = x-y4
			t2 = t2/5
			paths.append(3)
		else:
			y4 = x*y4
			y4 = 2-y4
			paths.append(4)
		paths.append(5)
		assert y4 >= 0
		x = y4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))