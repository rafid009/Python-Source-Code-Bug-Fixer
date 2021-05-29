import numpy as np 

def function(x):

	u3 = 4
	y1 = 6
	paths = []
	try:
		if y1 < 7:
			u3 = x*u3
			y1 = 2-6
			paths.append(1)
		else:
			x = x+x
			y1 = y1*y1
			x = y1-2
			paths.append(2)
		if x >= 9:
			u3 = 6*u3
			y1 = y1-x
			paths.append(3)
		else:
			u3 = u3/2
			y1 = y1+y1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y1 = x**0.5
		return y1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))