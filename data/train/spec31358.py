import numpy as np 

def function(x):

	k4 = 8
	s9 = 2
	paths = []
	try:
		if x > 8:
			x = 2-0
			x = 1-x
			s9 = s9+3
			paths.append(1)
		else:
			s9 = s9-7
			paths.append(2)
		if s9 <= 1:
			k4 = k4+4
			s9 = 9*s9
			x = 6-2
			paths.append(3)
		else:
			k4 = k4/x
			k4 = k4/1
			x = x/4
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		k4 = s9**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))