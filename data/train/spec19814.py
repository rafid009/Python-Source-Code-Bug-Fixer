import numpy as np 

def function(x):

	u3 = 9
	y0 = 0
	paths = []
	try:
		if x <= 8:
			u3 = x-1
			y0 = y0+0
			x = x/5
			paths.append(1)
		else:
			u3 = 4-y0
			u3 = 6*u3
			paths.append(2)
		if y0 > 8:
			u3 = 4+1
			y0 = 6*9
			y0 = 0-y0
			paths.append(3)
		else:
			u3 = x/u3
			u3 = 1*u3
			x = 7-2
			paths.append(4)
		paths.append(5)
		assert u3 >= 0
		x = u3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))