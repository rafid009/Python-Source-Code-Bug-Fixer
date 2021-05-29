import numpy as np 

def function(x):

	s8 = x
	u0 = 2
	paths = []
	try:
		if x < 8:
			x = 7+x
			paths.append(1)
		else:
			s8 = s8-9
			s8 = s8*9
			u0 = u0-u0
			paths.append(2)
		if u0 <= 4:
			u0 = x-3
			paths.append(3)
		else:
			x = 2*x
			x = 4/6
			x = u0*s8
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		u0 = s8**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))