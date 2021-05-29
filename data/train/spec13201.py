import numpy as np 

def function(x):

	s7 = x
	m7 = x
	paths = []
	try:
		if s7 >= 3:
			s7 = s7-3
			x = s7-1
			paths.append(1)
		else:
			s7 = x+5
			paths.append(2)
		if m7 < 4:
			x = 5*9
			x = 5-8
			paths.append(3)
		else:
			s7 = 3-x
			x = x+x
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