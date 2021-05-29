import numpy as np 

def function(x):

	s9 = x
	x1 = 1
	paths = []
	try:
		if s9 <= 9:
			x = x*6
			x1 = x1+2
			paths.append(1)
		else:
			s9 = x/9
			s9 = x*9
			paths.append(2)
		if s9 >= 1:
			x = x+2
			x1 = 0+4
			s9 = s9-0
			paths.append(3)
		else:
			x = x-4
			x1 = x1-x
			x1 = x1*9
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		s9 = s9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))