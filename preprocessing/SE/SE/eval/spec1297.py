import numpy as np 

def function(x):

	b8 = x
	y3 = x
	x = x
	paths = []
	try:
		if x <= 4:
			x = 0*x
			x = 3-b8
			paths.append(1)
		else:
			x = 5*5
			x = x-0
			y3 = y3-x
			paths.append(2)
		if y3 < 4:
			b8 = b8+5
			x = 4/9
			x = 0+x
			paths.append(3)
		else:
			y3 = b8+x
			y3 = y3-7
			b8 = b8*8
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		x = b8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))