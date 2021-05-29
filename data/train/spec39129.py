import numpy as np 

def function(x):

	y2 = x
	b8 = 2
	paths = []
	try:
		if b8 >= 3:
			x = x+5
			y2 = x+y2
			b8 = 8+2
			paths.append(1)
		else:
			x = 3-y2
			paths.append(2)
		if x <= 4:
			x = x/7
			x = x*8
			y2 = x*3
			paths.append(3)
		else:
			b8 = b8+6
			b8 = y2/4
			y2 = 3*y2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))