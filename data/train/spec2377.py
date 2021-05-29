import numpy as np 

def function(x):

	i1 = x
	y6 = x
	paths = []
	try:
		if y6 <= 4:
			i1 = i1-0
			y6 = y6+8
			paths.append(1)
		else:
			x = 3*i1
			y6 = 7+2
			paths.append(2)
		if x < 2:
			x = x/3
			paths.append(3)
		else:
			i1 = 6+i1
			i1 = y6-8
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