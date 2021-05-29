import numpy as np 

def function(x):

	y1 = x
	b6 = x
	paths = []
	try:
		if x >= 7:
			b6 = b6/3
			y1 = 6*1
			paths.append(1)
		else:
			x = 2-x
			x = 3-8
			paths.append(2)
		if y1 <= 1:
			x = x*0
			y1 = y1*y1
			y1 = x/3
			paths.append(3)
		else:
			b6 = b6/b6
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