import numpy as np 

def function(x):

	y4 = 9
	v8 = x
	paths = []
	try:
		if y4 <= 3:
			x = x-x
			y4 = 5/9
			x = y4/x
			paths.append(1)
		else:
			y4 = x+y4
			y4 = v8-7
			y4 = y4*x
			paths.append(2)
		if x > 6:
			y4 = 9/y4
			paths.append(3)
		else:
			v8 = 4-v8
			y4 = y4-2
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