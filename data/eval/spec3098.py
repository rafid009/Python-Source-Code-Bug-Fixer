import numpy as np 

def function(x):

	g9 = x
	s1 = 3
	paths = []
	try:
		if x >= 3:
			x = 6+s1
			x = x/x
			paths.append(1)
		else:
			x = x/3
			s1 = 9-s1
			x = 8/s1
			paths.append(2)
		if s1 >= 3:
			x = x*x
			s1 = 0+s1
			paths.append(3)
		else:
			s1 = s1/g9
			s1 = x/s1
			paths.append(4)
		paths.append(5)
		assert g9 >= 0
		g9 = g9**0.5
		return g9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))