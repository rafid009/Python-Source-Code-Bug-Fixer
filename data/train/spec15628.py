import numpy as np 

def function(x):

	j6 = 2
	y0 = x
	x = 4
	paths = []
	try:
		if y0 < 6:
			j6 = 3+j6
			paths.append(1)
		else:
			j6 = x+j6
			y0 = y0*y0
			j6 = y0+5
			paths.append(2)
		if y0 <= 0:
			j6 = j6/6
			x = x/x
			paths.append(3)
		else:
			j6 = j6+3
			y0 = 8+9
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		y0 = y0**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))