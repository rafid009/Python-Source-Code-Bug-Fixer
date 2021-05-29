import numpy as np 

def function(x):

	s9 = x
	q4 = 9
	paths = []
	try:
		if s9 <= 3:
			s9 = x-3
			s9 = x+s9
			s9 = s9+1
			paths.append(1)
		else:
			s9 = x/8
			q4 = 7*x
			paths.append(2)
		if x <= 0:
			s9 = s9-4
			x = x/8
			paths.append(3)
		else:
			s9 = s9-q4
			x = 5*4
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		q4 = s9**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))