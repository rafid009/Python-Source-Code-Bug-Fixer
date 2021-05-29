import numpy as np 

def function(x):

	b9 = 4
	s4 = 2
	paths = []
	try:
		if x > 8:
			b9 = 4/9
			paths.append(1)
		else:
			s4 = 1/9
			x = x+x
			paths.append(2)
		if x > 4:
			b9 = b9-5
			paths.append(3)
		else:
			x = 8*x
			s4 = 0-4
			b9 = 5/b9
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		s4 = s4**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))