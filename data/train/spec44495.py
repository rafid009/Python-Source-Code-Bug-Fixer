import numpy as np 

def function(x):

	q3 = 0
	s1 = 2
	paths = []
	try:
		if q3 > 4:
			q3 = q3*3
			paths.append(1)
		else:
			s1 = s1-4
			paths.append(2)
		if s1 <= 0:
			s1 = s1*3
			paths.append(3)
		else:
			q3 = q3*8
			s1 = s1-7
			q3 = q3-s1
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		q3 = s1**0.5
		return q3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))