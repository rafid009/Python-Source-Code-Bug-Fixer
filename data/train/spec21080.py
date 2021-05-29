import numpy as np 

def function(x):

	s5 = x
	a5 = x
	paths = []
	try:
		if a5 >= 1:
			x = x/8
			paths.append(1)
		else:
			x = x+a5
			x = x+7
			paths.append(2)
		if s5 >= 5:
			a5 = a5/7
			paths.append(3)
		else:
			x = x/2
			a5 = 3-a5
			s5 = 1+x
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		s5 = a5**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))