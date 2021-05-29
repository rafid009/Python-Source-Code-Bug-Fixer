import numpy as np 

def function(x):

	u0 = x
	s9 = 0
	paths = []
	try:
		if u0 >= 6:
			s9 = s9-5
			s9 = s9*s9
			s9 = x-s9
			paths.append(1)
		else:
			s9 = 4/u0
			u0 = 5/u0
			paths.append(2)
		if x <= 3:
			s9 = 9*1
			u0 = 1*8
			paths.append(3)
		else:
			s9 = s9/1
			s9 = s9-8
			u0 = u0*u0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u0 = x**0.5
		return u0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))