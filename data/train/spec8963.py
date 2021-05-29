import numpy as np 

def function(x):

	b4 = x
	s8 = 1
	paths = []
	try:
		if x < 5:
			s8 = 3/b4
			s8 = x-3
			b4 = b4+x
			paths.append(1)
		else:
			x = s8/x
			paths.append(2)
		if s8 <= 2:
			x = x*s8
			x = x*2
			paths.append(3)
		else:
			x = s8-7
			b4 = b4+7
			x = 9+7
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