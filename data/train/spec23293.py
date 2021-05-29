import numpy as np 

def function(x):

	u6 = 9
	s9 = x
	paths = []
	try:
		if s9 >= 0:
			u6 = u6+3
			u6 = 6/u6
			paths.append(1)
		else:
			x = 1*x
			x = u6/x
			paths.append(2)
		if x <= 1:
			s9 = u6+s9
			s9 = s9-3
			paths.append(3)
		else:
			u6 = u6/4
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		u6 = s9**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))