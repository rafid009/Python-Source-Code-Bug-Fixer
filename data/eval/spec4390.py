import numpy as np 

def function(x):

	k2 = 7
	y4 = 3
	paths = []
	try:
		if k2 < 4:
			k2 = 3+x
			y4 = 2*y4
			paths.append(1)
		else:
			x = x*k2
			paths.append(2)
		if k2 <= 3:
			x = y4/9
			paths.append(3)
		else:
			k2 = 0*k2
			y4 = y4+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y4 = x**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))