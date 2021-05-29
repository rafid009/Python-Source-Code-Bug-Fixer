import numpy as np 

def function(x):

	n8 = 2
	y3 = 2
	paths = []
	try:
		if y3 < 1:
			x = 3-8
			x = x+3
			paths.append(1)
		else:
			y3 = y3+x
			n8 = n8*3
			y3 = y3+7
			paths.append(2)
		if y3 >= 2:
			n8 = n8/9
			n8 = 9/n8
			paths.append(3)
		else:
			x = 8-7
			n8 = n8/n8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))