import numpy as np 

def function(x):

	s6 = x
	q5 = 7
	paths = []
	try:
		if q5 <= 6:
			s6 = 1/q5
			paths.append(1)
		else:
			s6 = s6-0
			s6 = s6+s6
			q5 = 2-q5
			paths.append(2)
		if s6 >= 1:
			q5 = s6-q5
			paths.append(3)
		else:
			s6 = s6*5
			x = 9*2
			paths.append(4)
		paths.append(5)
		assert q5 >= 0
		q5 = q5**0.5
		return q5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))