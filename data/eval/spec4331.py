import numpy as np 

def function(x):

	s9 = 5
	u4 = x
	paths = []
	try:
		if x < 7:
			x = x+6
			s9 = s9*2
			s9 = 8+7
			paths.append(1)
		else:
			u4 = 2+4
			paths.append(2)
		if x >= 2:
			s9 = 1+s9
			u4 = 8+u4
			s9 = s9*6
			paths.append(3)
		else:
			x = u4-0
			s9 = 4/7
			paths.append(4)
		paths.append(5)
		assert u4 >= 0
		s9 = u4**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))