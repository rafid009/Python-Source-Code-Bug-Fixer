import numpy as np 

def function(x):

	u9 = 7
	s5 = 6
	paths = []
	try:
		if u9 < 4:
			x = x-u9
			x = x/7
			u9 = 6+u9
			paths.append(1)
		else:
			u9 = 6-u9
			x = 5/x
			paths.append(2)
		if s5 <= 2:
			u9 = u9-7
			paths.append(3)
		else:
			u9 = u9*4
			s5 = s5/2
			u9 = u9/8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s5 = x**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))