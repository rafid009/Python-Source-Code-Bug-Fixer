import numpy as np 

def function(x):

	s4 = 1
	p3 = x
	x = x
	paths = []
	try:
		if x >= 2:
			x = x-2
			p3 = p3+x
			paths.append(1)
		else:
			x = 3-x
			s4 = x*2
			p3 = 9/p3
			paths.append(2)
		if x < 6:
			x = 6/x
			paths.append(3)
		else:
			x = x+7
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		s4 = p3**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))