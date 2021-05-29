import numpy as np 

def function(x):

	s0 = x
	u9 = 1
	paths = []
	try:
		if u9 >= 5:
			s0 = s0/7
			paths.append(1)
		else:
			s0 = s0*3
			paths.append(2)
		if s0 < 9:
			x = x/2
			s0 = 2*s0
			u9 = u9*s0
			paths.append(3)
		else:
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert u9 >= 0
		u9 = u9**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))