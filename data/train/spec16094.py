import numpy as np 

def function(x):

	s7 = 6
	l9 = 9
	paths = []
	try:
		if l9 <= 7:
			s7 = s7/1
			x = 9*x
			x = l9*l9
			paths.append(1)
		else:
			s7 = 1+s7
			paths.append(2)
		if x >= 1:
			x = l9/x
			paths.append(3)
		else:
			x = x*9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s7 = x**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))