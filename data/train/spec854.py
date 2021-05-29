import numpy as np 

def function(x):

	y1 = 1
	y4 = 4
	paths = []
	try:
		if y1 <= 4:
			x = x*y4
			paths.append(1)
		else:
			y4 = 1+y4
			x = 0/y4
			y4 = 5*y4
			paths.append(2)
		if x > 3:
			y4 = 7/2
			paths.append(3)
		else:
			y1 = x+4
			x = 7*7
			y4 = 8*y4
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y4 = y1**0.5
		return y4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))