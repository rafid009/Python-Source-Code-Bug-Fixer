import numpy as np 

def function(x):

	s4 = x
	u9 = 3
	paths = []
	try:
		if s4 <= 2:
			u9 = u9+3
			x = x*s4
			paths.append(1)
		else:
			s4 = s4/1
			u9 = u9/6
			paths.append(2)
		if x > 4:
			s4 = s4/6
			u9 = u9*4
			paths.append(3)
		else:
			s4 = x-s4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		u9 = s4**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))