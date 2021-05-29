import numpy as np 

def function(x):

	s2 = x
	u4 = x
	x = 6
	paths = []
	try:
		if s2 < 3:
			s2 = 9-8
			x = 6*x
			paths.append(1)
		else:
			x = u4/5
			u4 = 9/s2
			paths.append(2)
		if s2 >= 8:
			x = x*9
			u4 = 8+u4
			paths.append(3)
		else:
			s2 = x*7
			x = u4/3
			u4 = x+x
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		u4 = u4**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))