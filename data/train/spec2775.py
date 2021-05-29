import numpy as np 

def function(x):

	s8 = 7
	b6 = x
	paths = []
	try:
		if s8 >= 6:
			s8 = x-b6
			paths.append(1)
		else:
			x = x+b6
			paths.append(2)
		if x < 4:
			x = 9*1
			x = s8/x
			paths.append(3)
		else:
			b6 = b6/9
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		x = b6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))