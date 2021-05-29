import numpy as np 

def function(x):

	v7 = x
	s6 = x
	paths = []
	try:
		if x <= 1:
			s6 = s6/3
			v7 = v7-8
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if v7 <= 0:
			x = x-3
			paths.append(3)
		else:
			x = s6*4
			v7 = v7+1
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		v7 = s6**0.5
		return v7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))