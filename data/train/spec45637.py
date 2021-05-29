import numpy as np 

def function(x):

	j2 = x
	y6 = x
	paths = []
	try:
		if j2 < 1:
			x = 7+x
			j2 = 1/x
			y6 = 4/y6
			paths.append(1)
		else:
			y6 = 0-y6
			x = x*x
			paths.append(2)
		if y6 > 8:
			y6 = 0+y6
			paths.append(3)
		else:
			x = 8/x
			y6 = y6/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j2 = x**0.5
		return j2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))