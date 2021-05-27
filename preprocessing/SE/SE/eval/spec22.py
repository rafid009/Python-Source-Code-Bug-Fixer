import numpy as np 

def function(x):

	u6 = 7
	s1 = x
	paths = []
	try:
		if s1 >= 6:
			u6 = 2/u6
			paths.append(1)
		else:
			u6 = 0+4
			s1 = u6*s1
			x = x+s1
			paths.append(2)
		if x <= 6:
			u6 = x+x
			paths.append(3)
		else:
			s1 = s1*6
			u6 = u6+x
			u6 = u6+x
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		u6 = s1**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))