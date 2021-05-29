import numpy as np 

def function(x):

	w1 = x
	s5 = 6
	paths = []
	try:
		if s5 >= 3:
			w1 = 9*w1
			s5 = s5+s5
			paths.append(1)
		else:
			x = x*7
			x = 0*x
			paths.append(2)
		if s5 <= 7:
			w1 = 2/9
			x = x/9
			paths.append(3)
		else:
			s5 = x*5
			x = x*9
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