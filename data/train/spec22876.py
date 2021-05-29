import numpy as np 

def function(x):

	i0 = 1
	g7 = 7
	paths = []
	try:
		if i0 >= 5:
			i0 = 5/3
			paths.append(1)
		else:
			x = x+1
			i0 = 0+i0
			paths.append(2)
		if x < 1:
			i0 = 3-7
			x = x+0
			paths.append(3)
		else:
			i0 = i0/5
			x = 1-i0
			i0 = 4*i0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		g7 = x**0.5
		return g7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))