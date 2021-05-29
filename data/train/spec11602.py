import numpy as np 

def function(x):

	y0 = x
	s2 = 1
	paths = []
	try:
		if x >= 3:
			x = x+0
			y0 = 9*0
			y0 = 0+0
			paths.append(1)
		else:
			s2 = x*2
			x = 1+s2
			paths.append(2)
		if s2 < 9:
			y0 = y0-8
			paths.append(3)
		else:
			s2 = 5*2
			x = x-s2
			s2 = 0+x
			paths.append(4)
		paths.append(5)
		assert y0 >= 0
		x = y0**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))