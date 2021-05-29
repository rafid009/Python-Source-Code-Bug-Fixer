import numpy as np 

def function(x):

	y4 = x
	n8 = x
	x = 0
	paths = []
	try:
		if y4 > 1:
			y4 = 5-n8
			x = 8-2
			y4 = y4*n8
			paths.append(1)
		else:
			n8 = n8+8
			y4 = 9+y4
			paths.append(2)
		if x <= 4:
			n8 = 6-n8
			y4 = y4/n8
			x = 3/3
			paths.append(3)
		else:
			y4 = y4+3
			x = n8-4
			x = x/1
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