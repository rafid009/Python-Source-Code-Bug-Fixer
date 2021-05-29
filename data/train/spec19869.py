import numpy as np 

def function(x):

	b5 = 2
	s8 = x
	paths = []
	try:
		if x >= 0:
			x = 8+x
			paths.append(1)
		else:
			s8 = 4-1
			x = x/x
			paths.append(2)
		if b5 < 2:
			x = x-b5
			x = x*x
			paths.append(3)
		else:
			x = 4*x
			b5 = s8-2
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		x = b5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))