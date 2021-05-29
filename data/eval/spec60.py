import numpy as np 

def function(x):

	s7 = x
	q2 = 3
	paths = []
	try:
		if q2 > 7:
			q2 = q2+7
			paths.append(1)
		else:
			s7 = q2+x
			x = x*x
			s7 = s7+1
			paths.append(2)
		if x < 5:
			s7 = s7+s7
			q2 = q2+6
			q2 = q2+9
			paths.append(3)
		else:
			q2 = 3+8
			x = x+x
			q2 = 6/x
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		s7 = s7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))