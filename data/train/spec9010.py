import numpy as np 

def function(x):

	y1 = 6
	b9 = x
	paths = []
	try:
		if x >= 5:
			y1 = 6*x
			b9 = x+9
			paths.append(1)
		else:
			y1 = 5/x
			b9 = b9-b9
			b9 = b9-y1
			paths.append(2)
		if b9 > 1:
			y1 = 5*y1
			y1 = y1/6
			x = y1*x
			paths.append(3)
		else:
			y1 = 4+b9
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		y1 = y1**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))