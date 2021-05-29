import numpy as np 

def function(x):

	x6 = 6
	s7 = x
	paths = []
	try:
		if x6 < 1:
			x6 = x6+9
			x = 3+x
			x = s7+x6
			paths.append(1)
		else:
			x = x6+x
			x6 = 1*5
			x6 = s7-x
			paths.append(2)
		if x <= 2:
			s7 = x*5
			paths.append(3)
		else:
			x6 = 7+x6
			s7 = 4/7
			x = 4/4
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x6 = s7**0.5
		return x6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))