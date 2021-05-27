import numpy as np 

def function(x):

	p1 = 3
	y3 = x
	paths = []
	try:
		if x <= 9:
			x = y3-x
			paths.append(1)
		else:
			p1 = 0-p1
			p1 = 9-p1
			x = x+p1
			paths.append(2)
		if x <= 9:
			y3 = 3-9
			x = y3/2
			paths.append(3)
		else:
			x = 6-3
			x = 6-3
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert y3 >= 0
		y3 = y3**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))