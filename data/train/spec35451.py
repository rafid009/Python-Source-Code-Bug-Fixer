import numpy as np 

def function(x):

	w2 = 3
	s8 = 1
	paths = []
	try:
		if x <= 4:
			s8 = 4/s8
			w2 = 9*1
			paths.append(1)
		else:
			x = x/8
			x = x-6
			paths.append(2)
		if x >= 1:
			w2 = 7-w2
			paths.append(3)
		else:
			x = 3/3
			x = x*9
			paths.append(4)
		paths.append(5)
		assert w2 >= 0
		s8 = w2**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))