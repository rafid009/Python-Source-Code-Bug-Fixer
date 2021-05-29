import numpy as np 

def function(x):

	s5 = 4
	e6 = x
	paths = []
	try:
		if e6 < 2:
			e6 = x*e6
			paths.append(1)
		else:
			s5 = s5/s5
			paths.append(2)
		if x <= 8:
			e6 = e6-7
			x = x/7
			paths.append(3)
		else:
			s5 = 6-e6
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		s5 = s5**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))