import numpy as np 

def function(x):

	n1 = 5
	y8 = x
	paths = []
	try:
		if y8 < 7:
			y8 = y8+0
			y8 = 8+y8
			paths.append(1)
		else:
			x = x*5
			n1 = 5/n1
			x = n1+7
			paths.append(2)
		if x >= 7:
			y8 = 0+y8
			n1 = n1*9
			paths.append(3)
		else:
			y8 = 8/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n1 = x**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))