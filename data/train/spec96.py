import numpy as np 

def function(x):

	s5 = 6
	q4 = 8
	x = 5
	paths = []
	try:
		if x >= 1:
			s5 = x-q4
			x = 9+x
			paths.append(1)
		else:
			x = x*4
			paths.append(2)
		if s5 >= 4:
			q4 = 7/q4
			paths.append(3)
		else:
			s5 = s5/1
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