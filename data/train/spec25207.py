import numpy as np 

def function(x):

	n4 = 2
	s1 = x
	x = x
	paths = []
	try:
		if s1 >= 9:
			s1 = x*7
			paths.append(1)
		else:
			x = x-3
			n4 = 0/n4
			paths.append(2)
		if x < 4:
			x = 2-x
			paths.append(3)
		else:
			s1 = x-s1
			x = 3-4
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		x = s1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))