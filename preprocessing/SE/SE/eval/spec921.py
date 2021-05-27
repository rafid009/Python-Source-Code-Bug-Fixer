import numpy as np 

def function(x):

	b8 = x
	y1 = 4
	paths = []
	try:
		if b8 < 9:
			x = x+0
			paths.append(1)
		else:
			x = x+0
			b8 = b8+b8
			y1 = 4/x
			paths.append(2)
		if x > 6:
			b8 = b8+1
			b8 = b8/9
			paths.append(3)
		else:
			x = x*y1
			y1 = 6+y1
			b8 = x+b8
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