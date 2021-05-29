import numpy as np 

def function(x):

	s8 = x
	q9 = 6
	paths = []
	try:
		if x < 2:
			x = q9/x
			paths.append(1)
		else:
			s8 = 7/q9
			paths.append(2)
		if s8 >= 5:
			q9 = 0+1
			x = x-2
			paths.append(3)
		else:
			x = x*4
			s8 = s8+8
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