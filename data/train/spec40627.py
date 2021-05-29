import numpy as np 

def function(x):

	i1 = 7
	s6 = x
	x = 1
	paths = []
	try:
		if i1 < 4:
			i1 = x-x
			paths.append(1)
		else:
			i1 = i1/x
			s6 = s6/i1
			x = x-7
			paths.append(2)
		if i1 < 0:
			s6 = 6+0
			s6 = 5-8
			paths.append(3)
		else:
			x = x-7
			x = i1-7
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