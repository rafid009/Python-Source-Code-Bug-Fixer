import numpy as np 

def function(x):

	n8 = 2
	s1 = 2
	paths = []
	try:
		if s1 < 1:
			x = x-s1
			n8 = n8*s1
			paths.append(1)
		else:
			x = 3*x
			s1 = 2*x
			x = x-x
			paths.append(2)
		if s1 <= 6:
			s1 = n8/s1
			s1 = s1/3
			n8 = n8+x
			paths.append(3)
		else:
			n8 = 1+n8
			s1 = 5*s1
			n8 = x/n8
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