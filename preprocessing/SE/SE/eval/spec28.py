import numpy as np 

def function(x):

	s5 = x
	e3 = x
	paths = []
	try:
		if x > 9:
			s5 = 9+s5
			paths.append(1)
		else:
			x = x/2
			paths.append(2)
		if e3 >= 4:
			e3 = e3*1
			paths.append(3)
		else:
			s5 = 7-x
			e3 = s5+s5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s5 = x**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))