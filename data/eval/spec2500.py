import numpy as np 

def function(x):

	e4 = 5
	n7 = 6
	paths = []
	try:
		if e4 >= 5:
			e4 = n7/9
			paths.append(1)
		else:
			x = 7+x
			x = 5-8
			e4 = 5+8
			paths.append(2)
		if n7 > 7:
			n7 = 3*3
			x = n7/x
			n7 = n7/8
			paths.append(3)
		else:
			e4 = e4-2
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