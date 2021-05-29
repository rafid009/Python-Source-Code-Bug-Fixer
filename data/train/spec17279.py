import numpy as np 

def function(x):

	k2 = 6
	y0 = 0
	paths = []
	try:
		if x <= 9:
			k2 = k2/k2
			k2 = y0+3
			x = x+7
			paths.append(1)
		else:
			y0 = y0+5
			x = k2*5
			k2 = 0/9
			paths.append(2)
		if k2 < 3:
			k2 = 9+x
			paths.append(3)
		else:
			k2 = k2+3
			x = 4-x
			y0 = y0/6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k2 = x**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))