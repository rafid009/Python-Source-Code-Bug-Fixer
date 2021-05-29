import numpy as np 

def function(x):

	y4 = x
	v0 = x
	paths = []
	try:
		if v0 > 7:
			y4 = 3+y4
			x = 9*8
			x = 1/v0
			paths.append(1)
		else:
			x = x+7
			v0 = x+v0
			paths.append(2)
		if v0 < 2:
			y4 = y4*2
			y4 = y4/v0
			paths.append(3)
		else:
			v0 = 1+0
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