import numpy as np 

def function(x):

	n2 = x
	s7 = 6
	paths = []
	try:
		if n2 <= 6:
			s7 = s7*0
			x = x+s7
			paths.append(1)
		else:
			s7 = 0/s7
			paths.append(2)
		if s7 <= 3:
			x = 2+n2
			paths.append(3)
		else:
			s7 = 2/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))