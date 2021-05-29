import numpy as np 

def function(x):

	s8 = x
	i9 = x
	paths = []
	try:
		if i9 <= 8:
			x = 6/1
			s8 = s8/3
			paths.append(1)
		else:
			i9 = 3+i9
			paths.append(2)
		if s8 <= 7:
			s8 = s8-i9
			x = s8*x
			i9 = i9*9
			paths.append(3)
		else:
			s8 = s8*7
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		s8 = s8**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))