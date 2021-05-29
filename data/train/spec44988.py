import numpy as np 

def function(x):

	s4 = x
	q0 = x
	paths = []
	try:
		if x >= 5:
			q0 = 4/q0
			s4 = s4+x
			s4 = 9/8
			paths.append(1)
		else:
			x = q0+2
			paths.append(2)
		if x > 0:
			x = s4/5
			paths.append(3)
		else:
			x = 0-x
			x = s4/x
			paths.append(4)
		paths.append(5)
		assert q0 >= 0
		q0 = q0**0.5
		return q0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))