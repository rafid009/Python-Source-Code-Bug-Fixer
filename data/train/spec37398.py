import numpy as np 

def function(x):

	s4 = 5
	e0 = 8
	paths = []
	try:
		if s4 <= 6:
			e0 = s4+e0
			e0 = 6/e0
			paths.append(1)
		else:
			s4 = s4*x
			e0 = x+6
			e0 = e0*s4
			paths.append(2)
		if x > 7:
			s4 = s4*0
			e0 = s4*e0
			paths.append(3)
		else:
			e0 = x+e0
			paths.append(4)
		paths.append(5)
		assert e0 >= 0
		s4 = e0**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))