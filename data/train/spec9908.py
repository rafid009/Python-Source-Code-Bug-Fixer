import numpy as np 

def function(x):

	n4 = 6
	s1 = x
	paths = []
	try:
		if x <= 5:
			x = x*6
			paths.append(1)
		else:
			n4 = 7+n4
			s1 = s1+7
			paths.append(2)
		if s1 <= 4:
			n4 = n4*1
			n4 = n4+3
			paths.append(3)
		else:
			n4 = n4/n4
			s1 = s1-1
			s1 = s1*6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))