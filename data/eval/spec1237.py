import numpy as np 

def function(x):

	s6 = x
	n8 = 8
	paths = []
	try:
		if n8 >= 5:
			x = x*n8
			x = x*9
			n8 = 8+s6
			paths.append(1)
		else:
			n8 = s6+2
			paths.append(2)
		if x <= 5:
			n8 = x-7
			paths.append(3)
		else:
			s6 = 8/2
			n8 = 9+n8
			paths.append(4)
		paths.append(5)
		assert s6 >= 0
		n8 = s6**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))