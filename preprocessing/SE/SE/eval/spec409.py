import numpy as np 

def function(x):

	y2 = x
	s8 = 4
	paths = []
	try:
		if x < 2:
			y2 = 1/9
			y2 = y2+8
			x = s8-7
			paths.append(1)
		else:
			x = x*9
			x = 3-s8
			paths.append(2)
		if y2 < 3:
			s8 = s8+s8
			paths.append(3)
		else:
			y2 = y2*8
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		y2 = x**0.5
		return y2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))