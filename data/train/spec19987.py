import numpy as np 

def function(x):

	q9 = 5
	s1 = x
	paths = []
	try:
		if x <= 7:
			s1 = s1*4
			x = x*s1
			paths.append(1)
		else:
			q9 = q9+9
			s1 = s1*5
			s1 = x+s1
			paths.append(2)
		if s1 <= 3:
			q9 = s1-q9
			q9 = q9-x
			paths.append(3)
		else:
			x = 6-3
			q9 = 2-q9
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		x = s1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))