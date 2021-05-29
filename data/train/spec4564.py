import numpy as np 

def function(x):

	n6 = x
	s2 = 9
	x = x
	paths = []
	try:
		if x > 7:
			s2 = s2-n6
			n6 = x/5
			n6 = n6*2
			paths.append(1)
		else:
			s2 = s2*9
			paths.append(2)
		if s2 >= 0:
			s2 = s2*s2
			s2 = s2-4
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert n6 >= 0
		x = n6**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))