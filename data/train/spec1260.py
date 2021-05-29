import numpy as np 

def function(x):

	q8 = x
	s5 = 4
	paths = []
	try:
		if x <= 2:
			x = x+1
			s5 = q8*s5
			x = x-7
			paths.append(1)
		else:
			q8 = q8+5
			s5 = 5/x
			s5 = 1/q8
			paths.append(2)
		if s5 > 7:
			q8 = s5*0
			q8 = x-q8
			paths.append(3)
		else:
			x = x/s5
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