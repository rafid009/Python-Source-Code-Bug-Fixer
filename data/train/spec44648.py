import numpy as np 

def function(x):

	s4 = x
	u1 = 8
	paths = []
	try:
		if u1 < 5:
			x = s4+u1
			x = s4/x
			x = 7/4
			paths.append(1)
		else:
			s4 = 8*s4
			s4 = s4*u1
			x = s4+4
			paths.append(2)
		if x >= 3:
			u1 = 5+u1
			x = x/6
			paths.append(3)
		else:
			s4 = s4-1
			u1 = 3/u1
			u1 = x/6
			paths.append(4)
		paths.append(5)
		assert u1 >= 0
		u1 = u1**0.5
		return u1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))