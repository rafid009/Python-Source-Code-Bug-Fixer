import numpy as np 

def function(x):

	s2 = 7
	n5 = x
	paths = []
	try:
		if x > 5:
			s2 = s2+s2
			paths.append(1)
		else:
			x = x/2
			s2 = 7-s2
			paths.append(2)
		if x <= 3:
			x = 2-x
			x = 8+x
			n5 = 5/n5
			paths.append(3)
		else:
			x = 3/x
			x = 0-x
			n5 = s2+n5
			paths.append(4)
		paths.append(5)
		assert n5 >= 0
		x = n5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))