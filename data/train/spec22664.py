import numpy as np 

def function(x):

	s9 = 9
	q9 = x
	paths = []
	try:
		if x > 5:
			s9 = 8*s9
			x = 5-8
			paths.append(1)
		else:
			x = s9*q9
			q9 = x+q9
			paths.append(2)
		if s9 >= 8:
			x = 3+7
			x = 1*x
			paths.append(3)
		else:
			s9 = s9/6
			x = x*2
			paths.append(4)
		paths.append(5)
		assert q9 >= 0
		x = q9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))