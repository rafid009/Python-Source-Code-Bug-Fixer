import numpy as np 

def function(x):

	s2 = x
	v2 = 3
	paths = []
	try:
		if x >= 7:
			s2 = 1+x
			x = 3/7
			paths.append(1)
		else:
			v2 = v2-v2
			s2 = 8/x
			paths.append(2)
		if s2 < 4:
			v2 = 9*v2
			paths.append(3)
		else:
			x = s2-x
			x = x-x
			v2 = 5+5
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		v2 = s2**0.5
		return v2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))