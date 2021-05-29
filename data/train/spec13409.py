import numpy as np 

def function(x):

	s9 = x
	u3 = x
	paths = []
	try:
		if x >= 4:
			s9 = x+7
			paths.append(1)
		else:
			s9 = 0/s9
			u3 = s9-0
			u3 = 5/7
			paths.append(2)
		if x < 8:
			u3 = 2-9
			paths.append(3)
		else:
			x = x*3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s9 = x**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))