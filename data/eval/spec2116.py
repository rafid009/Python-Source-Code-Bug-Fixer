import numpy as np 

def function(x):

	s2 = x
	u4 = 6
	x = 5
	paths = []
	try:
		if s2 < 6:
			s2 = s2+2
			paths.append(1)
		else:
			u4 = x*u4
			u4 = 2/u4
			paths.append(2)
		if s2 < 2:
			x = x/7
			paths.append(3)
		else:
			x = x-1
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))