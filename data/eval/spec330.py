import numpy as np 

def function(x):

	x8 = x
	s1 = 6
	paths = []
	try:
		if x > 2:
			x8 = 7*9
			s1 = s1-9
			paths.append(1)
		else:
			x8 = x8+x8
			x = 5*9
			x8 = x8+8
			paths.append(2)
		if x <= 3:
			s1 = x8/2
			s1 = 3+s1
			x = 2-x
			paths.append(3)
		else:
			x8 = s1-x8
			s1 = s1/3
			paths.append(4)
		paths.append(5)
		assert x8 >= 0
		x = x8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))