import numpy as np 

def function(x):

	u5 = 1
	s6 = x
	paths = []
	try:
		if s6 <= 1:
			x = x-u5
			paths.append(1)
		else:
			s6 = 5-s6
			x = s6+0
			x = 5+s6
			paths.append(2)
		if x < 6:
			x = s6+x
			x = x+8
			paths.append(3)
		else:
			s6 = s6-x
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		x = s6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))