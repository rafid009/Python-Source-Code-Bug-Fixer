import numpy as np 

def function(x):

	y2 = x
	n6 = x
	paths = []
	try:
		if y2 < 5:
			y2 = 0*x
			y2 = y2*n6
			paths.append(1)
		else:
			x = 3+x
			paths.append(2)
		if x <= 4:
			y2 = y2+1
			n6 = n6/n6
			paths.append(3)
		else:
			n6 = n6+x
			n6 = n6*y2
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