import numpy as np 

def function(x):

	n2 = 6
	y2 = 3
	paths = []
	try:
		if n2 > 2:
			n2 = n2/3
			y2 = 3+y2
			n2 = n2+2
			paths.append(1)
		else:
			n2 = n2-n2
			y2 = y2+7
			x = 4+x
			paths.append(2)
		if y2 >= 0:
			y2 = 1+y2
			n2 = 9/n2
			paths.append(3)
		else:
			y2 = y2*x
			x = 1-9
			y2 = 8/y2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))