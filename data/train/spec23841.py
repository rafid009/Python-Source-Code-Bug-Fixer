import numpy as np 

def function(x):

	s4 = 1
	q9 = x
	paths = []
	try:
		if x <= 3:
			x = x/s4
			q9 = s4+7
			paths.append(1)
		else:
			q9 = 0-s4
			paths.append(2)
		if x > 3:
			q9 = q9*5
			s4 = 0+s4
			paths.append(3)
		else:
			q9 = q9+0
			q9 = q9/x
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		q9 = q9**0.5
		return q9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))