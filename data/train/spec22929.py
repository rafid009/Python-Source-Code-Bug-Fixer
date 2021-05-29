import numpy as np 

def function(x):

	s4 = x
	u3 = 1
	paths = []
	try:
		if s4 <= 9:
			x = 5/x
			u3 = u3+6
			x = 8-0
			paths.append(1)
		else:
			s4 = 5+s4
			s4 = s4+8
			paths.append(2)
		if s4 < 9:
			x = 0*s4
			paths.append(3)
		else:
			u3 = u3*3
			u3 = u3-0
			x = x*x
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		u3 = s4**0.5
		return u3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))