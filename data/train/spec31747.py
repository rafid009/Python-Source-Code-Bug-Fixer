import numpy as np 

def function(x):

	j2 = x
	s8 = x
	paths = []
	try:
		if j2 <= 5:
			x = 9+s8
			s8 = 7+s8
			paths.append(1)
		else:
			s8 = s8*3
			j2 = j2-1
			paths.append(2)
		if s8 > 6:
			j2 = 7/x
			x = s8*x
			paths.append(3)
		else:
			x = s8*8
			x = x-s8
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