import numpy as np 

def function(x):

	v7 = 7
	s5 = x
	paths = []
	try:
		if s5 <= 8:
			v7 = v7/v7
			v7 = 7*8
			v7 = 3/s5
			paths.append(1)
		else:
			s5 = x/s5
			x = x-0
			s5 = s5/1
			paths.append(2)
		if s5 < 8:
			s5 = s5+0
			x = v7+6
			x = x*3
			paths.append(3)
		else:
			s5 = s5-0
			v7 = 2-3
			x = s5-x
			paths.append(4)
		paths.append(5)
		assert v7 >= 0
		s5 = v7**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))