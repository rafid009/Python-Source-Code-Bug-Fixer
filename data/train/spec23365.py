import numpy as np 

def function(x):

	s5 = x
	n1 = 4
	paths = []
	try:
		if s5 <= 4:
			n1 = 4-n1
			n1 = 7*n1
			paths.append(1)
		else:
			s5 = 6*s5
			n1 = s5/5
			paths.append(2)
		if x >= 2:
			s5 = 8-s5
			x = 0+s5
			paths.append(3)
		else:
			s5 = 8*s5
			x = x+2
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		n1 = s5**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))