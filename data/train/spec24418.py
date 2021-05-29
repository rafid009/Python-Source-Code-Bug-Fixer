import numpy as np 

def function(x):

	n3 = 7
	s7 = 3
	paths = []
	try:
		if n3 <= 4:
			s7 = x-s7
			x = x*8
			n3 = n3+x
			paths.append(1)
		else:
			s7 = s7/x
			paths.append(2)
		if n3 >= 2:
			s7 = 1+x
			x = x-2
			x = x*0
			paths.append(3)
		else:
			x = x-0
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		s7 = s7**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))