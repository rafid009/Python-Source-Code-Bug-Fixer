import numpy as np 

def function(x):

	y3 = 5
	b0 = x
	paths = []
	try:
		if b0 <= 8:
			y3 = b0+1
			paths.append(1)
		else:
			x = x/y3
			paths.append(2)
		if x < 6:
			y3 = x-8
			x = y3-x
			paths.append(3)
		else:
			y3 = b0/y3
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		x = y3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))