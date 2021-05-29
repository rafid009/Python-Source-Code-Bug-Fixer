import numpy as np 

def function(x):

	b6 = x
	s1 = x
	paths = []
	try:
		if s1 >= 4:
			x = 6*x
			x = 8+1
			paths.append(1)
		else:
			s1 = 4*3
			paths.append(2)
		if s1 <= 1:
			x = x-3
			b6 = b6-4
			s1 = 3-s1
			paths.append(3)
		else:
			s1 = 4*b6
			s1 = s1-6
			paths.append(4)
		paths.append(5)
		assert b6 >= 0
		b6 = b6**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))