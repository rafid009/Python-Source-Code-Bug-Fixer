import numpy as np 

def function(x):

	s1 = x
	n8 = 0
	paths = []
	try:
		if s1 >= 8:
			s1 = s1/5
			paths.append(1)
		else:
			x = 3-s1
			x = x*x
			x = x+7
			paths.append(2)
		if x > 0:
			s1 = s1-6
			paths.append(3)
		else:
			s1 = 7/s1
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		n8 = s1**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))