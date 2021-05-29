import numpy as np 

def function(x):

	y2 = 1
	b4 = x
	paths = []
	try:
		if y2 > 2:
			b4 = 3+b4
			paths.append(1)
		else:
			x = 2*y2
			paths.append(2)
		if x > 4:
			x = 9/4
			y2 = y2+x
			y2 = 9+2
			paths.append(3)
		else:
			x = x+9
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))