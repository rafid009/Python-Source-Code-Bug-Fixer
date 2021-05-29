import numpy as np 

def function(x):

	n7 = x
	y4 = 2
	paths = []
	try:
		if n7 < 5:
			n7 = 7+7
			paths.append(1)
		else:
			y4 = 3+y4
			paths.append(2)
		if y4 < 9:
			y4 = y4/n7
			x = x*9
			paths.append(3)
		else:
			x = 6+5
			n7 = n7/6
			n7 = n7*y4
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