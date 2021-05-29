import numpy as np 

def function(x):

	s7 = x
	u7 = x
	paths = []
	try:
		if x < 6:
			u7 = u7-1
			paths.append(1)
		else:
			u7 = 8+u7
			s7 = 3-s7
			paths.append(2)
		if u7 < 6:
			x = 0+x
			s7 = s7-7
			s7 = 6/s7
			paths.append(3)
		else:
			u7 = u7-6
			u7 = 6/u7
			x = x*s7
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))