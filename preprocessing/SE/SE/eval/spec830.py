import numpy as np 

def function(x):

	u2 = x
	s6 = x
	paths = []
	try:
		if s6 >= 5:
			x = x+5
			u2 = s6*u2
			s6 = s6+u2
			paths.append(1)
		else:
			s6 = s6-2
			paths.append(2)
		if s6 < 4:
			x = x+9
			u2 = u2*9
			paths.append(3)
		else:
			u2 = s6+8
			u2 = 6+u2
			u2 = u2+s6
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		x = u2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))