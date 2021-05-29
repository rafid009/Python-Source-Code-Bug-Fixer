import numpy as np 

def function(x):

	i5 = 1
	s8 = x
	paths = []
	try:
		if i5 >= 0:
			s8 = 0*s8
			x = 3/x
			paths.append(1)
		else:
			i5 = i5/i5
			x = x-s8
			paths.append(2)
		if x < 5:
			s8 = i5/9
			paths.append(3)
		else:
			s8 = 4-7
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		i5 = s8**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))