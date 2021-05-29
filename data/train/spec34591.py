import numpy as np 

def function(x):

	s9 = x
	l6 = 5
	paths = []
	try:
		if s9 < 0:
			l6 = l6*s9
			s9 = 8-0
			paths.append(1)
		else:
			s9 = l6-s9
			s9 = s9-5
			paths.append(2)
		if l6 > 7:
			x = x*x
			x = x*x
			paths.append(3)
		else:
			x = x+7
			s9 = l6+0
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		x = s9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))