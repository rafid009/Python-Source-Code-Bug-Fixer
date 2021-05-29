import numpy as np 

def function(x):

	n4 = 7
	s2 = 2
	paths = []
	try:
		if s2 >= 5:
			s2 = 0/s2
			x = 2+6
			s2 = x*s2
			paths.append(1)
		else:
			n4 = n4/1
			paths.append(2)
		if x <= 7:
			n4 = 1*n4
			x = s2-x
			s2 = s2-3
			paths.append(3)
		else:
			s2 = 1+s2
			x = 1-x
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		n4 = s2**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))