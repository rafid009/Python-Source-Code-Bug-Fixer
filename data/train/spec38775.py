import numpy as np 

def function(x):

	b4 = 3
	y1 = x
	x = x
	paths = []
	try:
		if x > 0:
			y1 = b4*x
			paths.append(1)
		else:
			x = x+4
			x = x*1
			paths.append(2)
		if x < 7:
			x = b4-x
			x = x/b4
			paths.append(3)
		else:
			y1 = b4*y1
			b4 = y1-5
			paths.append(4)
		paths.append(5)
		assert y1 >= 0
		b4 = y1**0.5
		return b4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))