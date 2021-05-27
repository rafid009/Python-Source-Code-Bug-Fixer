import numpy as np 

def function(x):

	y3 = 7
	r3 = 1
	x = x
	paths = []
	try:
		if x <= 1:
			y3 = 0-0
			x = x*5
			r3 = r3/6
			paths.append(1)
		else:
			y3 = 6/y3
			x = x*5
			paths.append(2)
		if y3 < 8:
			x = x*2
			y3 = 4+r3
			paths.append(3)
		else:
			x = y3*x
			y3 = 4+y3
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