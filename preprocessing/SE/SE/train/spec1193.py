import numpy as np 

def function(x):

	s6 = x
	j3 = 5
	paths = []
	try:
		if s6 < 2:
			x = 0-x
			x = 0-3
			paths.append(1)
		else:
			s6 = x/8
			j3 = j3*j3
			s6 = 6*s6
			paths.append(2)
		if s6 < 6:
			x = x-1
			paths.append(3)
		else:
			j3 = j3-1
			j3 = j3-5
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		j3 = s6**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))