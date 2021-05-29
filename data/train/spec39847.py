import numpy as np 

def function(x):

	y1 = x
	s5 = x
	paths = []
	try:
		if y1 < 9:
			y1 = 5/y1
			x = 3*4
			y1 = 6/x
			paths.append(1)
		else:
			x = 6/9
			paths.append(2)
		if s5 >= 3:
			s5 = s5/5
			paths.append(3)
		else:
			s5 = s5-7
			s5 = x+s5
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		s5 = s5**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))