import numpy as np 

def function(x):

	j3 = x
	n8 = 5
	paths = []
	try:
		if x >= 1:
			x = x-n8
			x = 2+9
			j3 = 1/j3
			paths.append(1)
		else:
			x = x*7
			x = x/8
			paths.append(2)
		if x <= 7:
			j3 = 8/j3
			n8 = 8-n8
			paths.append(3)
		else:
			n8 = n8*4
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