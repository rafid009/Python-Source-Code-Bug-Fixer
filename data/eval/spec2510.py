import numpy as np 

def function(x):

	x2 = x
	y1 = x
	paths = []
	try:
		if x <= 2:
			x2 = 0/6
			paths.append(1)
		else:
			x2 = x*6
			x2 = y1*7
			x2 = 8/9
			paths.append(2)
		if x > 2:
			x2 = 6/x2
			paths.append(3)
		else:
			x = x+x2
			x2 = 8/5
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		x2 = y1**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))