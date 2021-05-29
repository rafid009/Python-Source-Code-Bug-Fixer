import numpy as np 

def function(x):

	s6 = x
	u4 = x
	paths = []
	try:
		if u4 >= 4:
			x = x*6
			x = x-s6
			x = 5-x
			paths.append(1)
		else:
			u4 = 3/4
			u4 = u4-9
			paths.append(2)
		if u4 >= 0:
			x = x+8
			s6 = u4+u4
			paths.append(3)
		else:
			x = s6*s6
			x = 0*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))