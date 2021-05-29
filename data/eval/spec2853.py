import numpy as np 

def function(x):

	y7 = 5
	x1 = x
	x = x
	paths = []
	try:
		if x1 < 9:
			y7 = x-y7
			x = 6+5
			x = x/2
			paths.append(1)
		else:
			x1 = x1-x1
			x1 = x1-6
			x = 3-x
			paths.append(2)
		if y7 <= 5:
			y7 = x+x1
			y7 = x*4
			x = x+0
			paths.append(3)
		else:
			x1 = x1+4
			y7 = x+6
			x1 = x1+2
			paths.append(4)
		paths.append(5)
		assert y7 >= 0
		x1 = y7**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))