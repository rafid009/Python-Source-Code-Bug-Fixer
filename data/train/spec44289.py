import numpy as np 

def function(x):

	s9 = x
	l2 = 6
	paths = []
	try:
		if s9 > 2:
			l2 = s9-s9
			s9 = s9*0
			x = x/7
			paths.append(1)
		else:
			x = 9+l2
			paths.append(2)
		if x <= 9:
			x = x+9
			l2 = l2-0
			paths.append(3)
		else:
			x = x/2
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		l2 = s9**0.5
		return l2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))