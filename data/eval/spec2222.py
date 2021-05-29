import numpy as np 

def function(x):

	s6 = 1
	q9 = x
	paths = []
	try:
		if q9 >= 8:
			x = x/2
			paths.append(1)
		else:
			q9 = x+2
			q9 = q9*9
			q9 = 7*q9
			paths.append(2)
		if x > 8:
			x = x*8
			paths.append(3)
		else:
			s6 = x/9
			x = x*3
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		s6 = q9**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))