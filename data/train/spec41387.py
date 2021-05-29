import numpy as np 

def function(x):

	l0 = 8
	s6 = x
	x = x
	paths = []
	try:
		if s6 > 5:
			l0 = l0+x
			x = x*5
			paths.append(1)
		else:
			l0 = s6*0
			s6 = x-0
			paths.append(2)
		if x <= 7:
			l0 = l0+l0
			paths.append(3)
		else:
			x = 9+3
			x = 3/x
			x = x+0
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		s6 = s6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))