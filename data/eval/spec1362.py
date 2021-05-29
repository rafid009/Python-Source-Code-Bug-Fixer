import numpy as np 

def function(x):

	u6 = 5
	s6 = 8
	paths = []
	try:
		if s6 <= 3:
			s6 = s6+x
			s6 = 9/s6
			paths.append(1)
		else:
			s6 = s6/1
			paths.append(2)
		if s6 < 8:
			x = 2+s6
			x = s6*s6
			paths.append(3)
		else:
			u6 = 6*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))