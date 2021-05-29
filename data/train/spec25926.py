import numpy as np 

def function(x):

	e4 = x
	n5 = 6
	paths = []
	try:
		if e4 > 3:
			n5 = n5+6
			n5 = x/8
			n5 = n5-4
			paths.append(1)
		else:
			e4 = e4/6
			e4 = 7*4
			e4 = e4/9
			paths.append(2)
		if n5 <= 9:
			n5 = 7+e4
			paths.append(3)
		else:
			n5 = 6/3
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