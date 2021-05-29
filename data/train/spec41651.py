import numpy as np 

def function(x):

	s9 = 5
	b7 = 3
	paths = []
	try:
		if x < 5:
			b7 = 8/b7
			x = x/6
			b7 = b7+4
			paths.append(1)
		else:
			s9 = 6*s9
			b7 = b7-b7
			s9 = 1-s9
			paths.append(2)
		if s9 >= 1:
			s9 = s9/s9
			b7 = b7+2
			paths.append(3)
		else:
			x = s9/x
			x = 3/x
			x = 2+1
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