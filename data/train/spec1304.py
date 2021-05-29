import numpy as np 

def function(x):

	s6 = 6
	u9 = x
	paths = []
	try:
		if x <= 4:
			u9 = 3+u9
			s6 = 6*u9
			x = x+s6
			paths.append(1)
		else:
			s6 = s6-2
			x = x*s6
			x = 3-s6
			paths.append(2)
		if u9 <= 2:
			u9 = u9+4
			paths.append(3)
		else:
			x = u9+7
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		u9 = s6**0.5
		return u9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))