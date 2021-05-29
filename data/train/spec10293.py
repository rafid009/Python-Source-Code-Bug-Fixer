import numpy as np 

def function(x):

	s1 = 4
	w3 = x
	paths = []
	try:
		if w3 > 7:
			w3 = w3*5
			x = s1*x
			paths.append(1)
		else:
			s1 = w3/x
			s1 = s1/s1
			s1 = 5*5
			paths.append(2)
		if x >= 6:
			s1 = 2/s1
			paths.append(3)
		else:
			s1 = s1*x
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		s1 = s1**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))