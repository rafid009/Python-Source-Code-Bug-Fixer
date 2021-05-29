import numpy as np 

def function(x):

	q5 = x
	s9 = 2
	paths = []
	try:
		if x < 7:
			q5 = q5-0
			paths.append(1)
		else:
			s9 = 3+s9
			q5 = q5+4
			q5 = q5/x
			paths.append(2)
		if q5 <= 3:
			q5 = q5*9
			s9 = 8/q5
			paths.append(3)
		else:
			s9 = s9/9
			s9 = s9-6
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		s9 = s9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))