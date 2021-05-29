import numpy as np 

def function(x):

	y3 = x
	x2 = 8
	paths = []
	try:
		if y3 >= 4:
			x2 = 7/x2
			x = x/3
			x = 4/6
			paths.append(1)
		else:
			x = x*y3
			x = 1-x
			x2 = x2-2
			paths.append(2)
		if y3 < 9:
			x2 = x+x2
			paths.append(3)
		else:
			y3 = x2+y3
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x = x2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))