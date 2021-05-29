import numpy as np 

def function(x):

	k5 = x
	s6 = x
	paths = []
	try:
		if k5 <= 4:
			k5 = x*5
			paths.append(1)
		else:
			x = x+6
			x = x*x
			paths.append(2)
		if s6 <= 1:
			x = 1-x
			x = x/9
			paths.append(3)
		else:
			x = s6+5
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		s6 = s6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))