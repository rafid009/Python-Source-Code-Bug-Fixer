import numpy as np 

def function(x):

	s8 = 2
	q9 = 1
	paths = []
	try:
		if x > 3:
			x = x+2
			q9 = x*1
			paths.append(1)
		else:
			s8 = s8+x
			q9 = q9/q9
			paths.append(2)
		if s8 >= 4:
			q9 = q9*q9
			q9 = q9*9
			paths.append(3)
		else:
			x = x/9
			s8 = x-q9
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		s8 = s8**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))