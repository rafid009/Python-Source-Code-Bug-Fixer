import numpy as np 

def function(x):

	q7 = 7
	s2 = x
	paths = []
	try:
		if x > 7:
			q7 = 1+q7
			paths.append(1)
		else:
			s2 = x-3
			s2 = s2-q7
			q7 = 0-q7
			paths.append(2)
		if q7 <= 6:
			x = x*7
			q7 = 0+7
			paths.append(3)
		else:
			x = 9*9
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))