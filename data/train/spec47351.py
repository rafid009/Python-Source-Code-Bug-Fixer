import numpy as np 

def function(x):

	j2 = 0
	s7 = x
	paths = []
	try:
		if s7 >= 2:
			j2 = 3+8
			j2 = j2+3
			paths.append(1)
		else:
			s7 = s7/3
			x = x/1
			x = s7*j2
			paths.append(2)
		if s7 >= 9:
			s7 = 4-s7
			s7 = s7-s7
			paths.append(3)
		else:
			j2 = 8*j2
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))