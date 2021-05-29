import numpy as np 

def function(x):

	s8 = x
	e8 = 1
	paths = []
	try:
		if e8 > 5:
			x = 0/5
			s8 = s8+4
			s8 = 3+s8
			paths.append(1)
		else:
			e8 = 4*s8
			paths.append(2)
		if s8 >= 4:
			s8 = 0-s8
			s8 = 9-s8
			s8 = s8/8
			paths.append(3)
		else:
			x = x-e8
			x = x/3
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		e8 = e8**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))