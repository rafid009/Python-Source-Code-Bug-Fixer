import numpy as np 

def function(x):

	y4 = x
	b6 = x
	x = x
	paths = []
	try:
		if y4 < 7:
			y4 = 4-y4
			x = b6-8
			x = 7*y4
			paths.append(1)
		else:
			b6 = y4/y4
			x = x*1
			x = x+8
			paths.append(2)
		if x >= 2:
			x = 7/x
			y4 = b6+9
			y4 = y4+8
			paths.append(3)
		else:
			y4 = y4*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))