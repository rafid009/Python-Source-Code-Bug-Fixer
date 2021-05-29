import numpy as np 

def function(x):

	u9 = x
	s0 = x
	paths = []
	try:
		if u9 > 6:
			s0 = 9-s0
			x = x*x
			u9 = 1-u9
			paths.append(1)
		else:
			x = u9/x
			s0 = s0/9
			s0 = x+u9
			paths.append(2)
		if x < 5:
			x = x-0
			x = 7*4
			paths.append(3)
		else:
			s0 = 3-s0
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