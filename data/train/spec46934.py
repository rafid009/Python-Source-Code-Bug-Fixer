import numpy as np 

def function(x):

	u1 = 4
	s8 = 4
	paths = []
	try:
		if s8 >= 6:
			x = 2+x
			s8 = s8/u1
			x = 0*x
			paths.append(1)
		else:
			u1 = 5/u1
			s8 = s8+9
			paths.append(2)
		if u1 < 0:
			s8 = 6*s8
			u1 = 0+1
			s8 = 3*x
			paths.append(3)
		else:
			x = 9-u1
			u1 = u1-4
			x = x-5
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		x = u1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))