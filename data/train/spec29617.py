import numpy as np 

def function(x):

	s5 = 1
	n1 = x
	paths = []
	try:
		if x > 5:
			x = x/2
			s5 = 1/s5
			paths.append(1)
		else:
			x = x-9
			paths.append(2)
		if n1 >= 2:
			n1 = 3*4
			n1 = s5*4
			n1 = x-4
			paths.append(3)
		else:
			x = x+4
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))