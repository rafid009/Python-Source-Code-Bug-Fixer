import numpy as np 

def function(x):

	y3 = x
	s4 = 2
	paths = []
	try:
		if y3 <= 4:
			s4 = 1/y3
			x = y3/3
			paths.append(1)
		else:
			y3 = y3-s4
			x = 9-y3
			y3 = y3+0
			paths.append(2)
		if x <= 0:
			y3 = 8*s4
			paths.append(3)
		else:
			x = y3-7
			s4 = 6+s4
			x = 2-s4
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