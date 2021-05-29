import numpy as np 

def function(x):

	b6 = x
	s8 = 4
	paths = []
	try:
		if s8 < 1:
			s8 = 4+x
			paths.append(1)
		else:
			b6 = 2*b6
			paths.append(2)
		if b6 <= 7:
			s8 = x*7
			s8 = 9+x
			paths.append(3)
		else:
			b6 = 8/x
			x = b6+x
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		x = s8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))