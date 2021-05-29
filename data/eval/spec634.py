import numpy as np 

def function(x):

	s1 = x
	n7 = x
	x = 1
	paths = []
	try:
		if n7 <= 4:
			n7 = n7-n7
			n7 = n7+2
			x = 6+x
			paths.append(1)
		else:
			x = 8-x
			n7 = 4+n7
			paths.append(2)
		if n7 > 4:
			x = s1+x
			s1 = 4-s1
			paths.append(3)
		else:
			s1 = 0-s1
			x = x+5
			n7 = 9*n7
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