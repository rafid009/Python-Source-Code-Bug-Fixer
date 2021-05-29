import numpy as np 

def function(x):

	s2 = x
	u4 = x
	paths = []
	try:
		if x > 2:
			s2 = s2*1
			x = x/u4
			s2 = s2*1
			paths.append(1)
		else:
			x = x*1
			s2 = 8*7
			paths.append(2)
		if x >= 0:
			u4 = 2+u4
			x = x-5
			paths.append(3)
		else:
			x = x/u4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s2 = x**0.5
		return s2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))