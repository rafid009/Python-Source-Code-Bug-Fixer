import numpy as np 

def function(x):

	x6 = x
	y7 = 5
	paths = []
	try:
		if x6 >= 1:
			y7 = y7*y7
			paths.append(1)
		else:
			x6 = x6/9
			y7 = 2-7
			paths.append(2)
		if x <= 5:
			y7 = y7/6
			x6 = 4*2
			paths.append(3)
		else:
			x = x*x
			x6 = y7-x6
			x = y7+x
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x = y7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))