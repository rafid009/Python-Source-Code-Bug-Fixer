import numpy as np 

def function(x):

	u7 = 2
	s7 = x
	x = 9
	paths = []
	try:
		if s7 < 6:
			s7 = s7+5
			u7 = u7+5
			paths.append(1)
		else:
			s7 = 3*s7
			u7 = u7-3
			u7 = x*7
			paths.append(2)
		if s7 > 8:
			u7 = u7+u7
			x = u7+s7
			paths.append(3)
		else:
			x = x-x
			s7 = 7*9
			x = 2-5
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