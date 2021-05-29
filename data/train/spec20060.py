import numpy as np 

def function(x):

	q0 = x
	s9 = x
	paths = []
	try:
		if q0 < 2:
			x = 9/x
			s9 = s9+3
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if q0 <= 7:
			q0 = 8+q0
			s9 = 2*s9
			paths.append(3)
		else:
			q0 = 7+s9
			x = 8*3
			s9 = 5/x
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		q0 = s9**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))