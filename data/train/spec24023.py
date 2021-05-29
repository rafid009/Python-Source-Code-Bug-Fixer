import numpy as np 

def function(x):

	k7 = x
	s8 = x
	paths = []
	try:
		if k7 < 3:
			s8 = 5+x
			k7 = 6/k7
			k7 = k7/k7
			paths.append(1)
		else:
			x = 9/1
			x = x+6
			paths.append(2)
		if s8 < 4:
			s8 = 1-s8
			k7 = k7+x
			paths.append(3)
		else:
			x = k7-9
			s8 = s8-s8
			k7 = k7-s8
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		x = s8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))