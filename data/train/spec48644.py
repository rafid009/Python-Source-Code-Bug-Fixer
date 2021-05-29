import numpy as np 

def function(x):

	y2 = 7
	b9 = x
	paths = []
	try:
		if b9 < 2:
			b9 = 4*x
			x = x+x
			b9 = b9-5
			paths.append(1)
		else:
			y2 = y2-0
			x = b9-5
			paths.append(2)
		if y2 < 9:
			x = x-5
			x = x+x
			y2 = 2/x
			paths.append(3)
		else:
			y2 = x+y2
			y2 = b9/y2
			paths.append(4)
		paths.append(5)
		assert y2 >= 0
		b9 = y2**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))