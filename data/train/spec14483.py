import numpy as np 

def function(x):

	n2 = x
	y8 = x
	x = 2
	paths = []
	try:
		if y8 > 7:
			y8 = 4/y8
			y8 = y8+7
			x = n2-n2
			paths.append(1)
		else:
			x = n2-1
			x = x/8
			x = x/n2
			paths.append(2)
		if n2 >= 1:
			x = 5-x
			n2 = 0-n2
			n2 = 6+4
			paths.append(3)
		else:
			y8 = 7+0
			paths.append(4)
		paths.append(5)
		assert n2 >= 0
		x = n2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))