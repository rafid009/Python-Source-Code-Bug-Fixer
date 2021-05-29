import numpy as np 

def function(x):

	s0 = x
	l1 = x
	paths = []
	try:
		if x >= 7:
			l1 = l1+1
			s0 = l1*s0
			paths.append(1)
		else:
			s0 = 9/9
			x = 0+8
			paths.append(2)
		if l1 >= 4:
			l1 = l1*s0
			l1 = 3-7
			x = x-s0
			paths.append(3)
		else:
			l1 = 3*l1
			x = l1+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		l1 = x**0.5
		return l1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))