import numpy as np 

def function(x):

	s4 = x
	q5 = 9
	paths = []
	try:
		if x <= 0:
			q5 = q5/8
			x = 0-x
			paths.append(1)
		else:
			s4 = 5*s4
			paths.append(2)
		if q5 >= 4:
			s4 = s4/x
			paths.append(3)
		else:
			q5 = q5-7
			x = q5/x
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		s4 = q5**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))