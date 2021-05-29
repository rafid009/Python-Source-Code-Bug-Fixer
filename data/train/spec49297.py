import numpy as np 

def function(x):

	y3 = 3
	p1 = x
	x = 1
	paths = []
	try:
		if x < 5:
			x = y3/p1
			y3 = p1+6
			y3 = 9+2
			paths.append(1)
		else:
			x = x-2
			p1 = p1-7
			paths.append(2)
		if y3 <= 5:
			y3 = 8+y3
			y3 = p1+p1
			paths.append(3)
		else:
			x = x/5
			p1 = p1+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y3 = x**0.5
		return y3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))