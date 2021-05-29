import numpy as np 

def function(x):

	j2 = 9
	y0 = 2
	paths = []
	try:
		if x < 9:
			j2 = j2+y0
			paths.append(1)
		else:
			x = 5-x
			y0 = 0/y0
			paths.append(2)
		if j2 >= 4:
			j2 = j2+j2
			x = 4*x
			y0 = y0+x
			paths.append(3)
		else:
			y0 = 6*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y0 = x**0.5
		return y0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))