import numpy as np 

def function(x):

	a6 = 7
	s6 = x
	paths = []
	try:
		if x >= 5:
			s6 = s6+1
			paths.append(1)
		else:
			s6 = 3/s6
			paths.append(2)
		if s6 >= 1:
			x = s6*0
			s6 = 2/s6
			paths.append(3)
		else:
			x = x+6
			a6 = 3+s6
			x = x*x
			paths.append(4)
		paths.append(5)
		assert a6 >= 0
		s6 = a6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))