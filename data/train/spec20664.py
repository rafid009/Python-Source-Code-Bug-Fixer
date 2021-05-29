import numpy as np 

def function(x):

	s6 = x
	u5 = 7
	paths = []
	try:
		if u5 > 3:
			x = 1+7
			paths.append(1)
		else:
			s6 = s6/x
			x = u5+u5
			paths.append(2)
		if u5 > 5:
			x = x/1
			paths.append(3)
		else:
			s6 = s6/9
			u5 = u5-0
			x = 3*x
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		s6 = s6**0.5
		return s6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))