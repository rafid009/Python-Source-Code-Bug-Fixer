import numpy as np 

def function(x):

	y6 = x
	n5 = 6
	paths = []
	try:
		if n5 >= 8:
			n5 = y6-0
			y6 = n5/2
			x = n5*x
			paths.append(1)
		else:
			x = 5/x
			paths.append(2)
		if n5 < 4:
			y6 = n5+4
			x = x+x
			paths.append(3)
		else:
			y6 = 2*1
			x = x+x
			n5 = n5/2
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