import numpy as np 

def function(x):

	n4 = x
	y1 = 8
	paths = []
	try:
		if n4 <= 7:
			y1 = 5*y1
			paths.append(1)
		else:
			y1 = 2-y1
			paths.append(2)
		if x > 0:
			y1 = 5+5
			x = x+n4
			x = 5-y1
			paths.append(3)
		else:
			x = x*0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))