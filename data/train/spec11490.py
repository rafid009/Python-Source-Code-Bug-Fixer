import numpy as np 

def function(x):

	g8 = 0
	s1 = x
	paths = []
	try:
		if x >= 1:
			s1 = 6-s1
			paths.append(1)
		else:
			x = x-4
			s1 = g8-s1
			g8 = g8-s1
			paths.append(2)
		if x < 4:
			s1 = s1*8
			paths.append(3)
		else:
			x = s1+7
			g8 = g8+g8
			s1 = 8/s1
			paths.append(4)
		paths.append(5)
		assert g8 >= 0
		x = g8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))