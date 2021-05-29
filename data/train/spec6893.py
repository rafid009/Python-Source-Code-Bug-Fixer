import numpy as np 

def function(x):

	s1 = 7
	n1 = x
	paths = []
	try:
		if x >= 8:
			x = n1+x
			s1 = 0+s1
			n1 = 1*n1
			paths.append(1)
		else:
			n1 = n1*9
			n1 = n1-5
			s1 = s1*x
			paths.append(2)
		if x > 8:
			s1 = s1+3
			x = x-s1
			paths.append(3)
		else:
			x = 4+x
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		x = n1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))