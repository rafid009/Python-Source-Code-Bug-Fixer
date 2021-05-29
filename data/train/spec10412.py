import numpy as np 

def function(x):

	q6 = 3
	s1 = 3
	paths = []
	try:
		if x < 4:
			s1 = 5-s1
			paths.append(1)
		else:
			s1 = s1-q6
			paths.append(2)
		if x < 7:
			q6 = 4-q6
			q6 = x*4
			paths.append(3)
		else:
			s1 = s1/3
			s1 = s1+6
			x = x*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q6 = x**0.5
		return q6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))