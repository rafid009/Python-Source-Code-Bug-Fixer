import numpy as np 

def function(x):

	n7 = 0
	s8 = 1
	paths = []
	try:
		if x > 1:
			s8 = s8-n7
			x = x*3
			s8 = 4+x
			paths.append(1)
		else:
			n7 = s8-6
			s8 = s8/9
			paths.append(2)
		if n7 >= 4:
			x = x/5
			x = 1/x
			paths.append(3)
		else:
			n7 = n7*6
			x = 5/x
			paths.append(4)
		paths.append(5)
		assert n7 >= 0
		s8 = n7**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))