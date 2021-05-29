import numpy as np 

def function(x):

	s1 = 7
	q6 = 9
	paths = []
	try:
		if x < 9:
			s1 = s1-8
			q6 = q6-6
			paths.append(1)
		else:
			x = x/s1
			s1 = s1+3
			x = q6+1
			paths.append(2)
		if q6 <= 7:
			q6 = 1+9
			q6 = 3-q6
			paths.append(3)
		else:
			x = x+5
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		s1 = s1**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))