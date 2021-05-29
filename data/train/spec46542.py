import numpy as np 

def function(x):

	s6 = 9
	n1 = 7
	paths = []
	try:
		if x > 0:
			x = 9-x
			n1 = 2-5
			n1 = n1*s6
			paths.append(1)
		else:
			x = 7*x
			n1 = n1/4
			n1 = 1*n1
			paths.append(2)
		if n1 >= 2:
			n1 = 6+n1
			paths.append(3)
		else:
			s6 = 2+s6
			n1 = n1/6
			s6 = x+s6
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