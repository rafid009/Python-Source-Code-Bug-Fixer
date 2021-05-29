import numpy as np 

def function(x):

	r0 = 7
	n5 = 1
	paths = []
	try:
		if x <= 7:
			n5 = n5*9
			paths.append(1)
		else:
			x = x+8
			x = n5*x
			paths.append(2)
		if x >= 6:
			n5 = n5/6
			paths.append(3)
		else:
			x = x+1
			n5 = n5/n5
			n5 = 9/3
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