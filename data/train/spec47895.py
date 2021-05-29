import numpy as np 

def function(x):

	b9 = x
	s7 = x
	paths = []
	try:
		if b9 >= 0:
			s7 = s7+b9
			b9 = b9-2
			x = x-9
			paths.append(1)
		else:
			b9 = 8-9
			s7 = 8-s7
			b9 = 9/1
			paths.append(2)
		if s7 > 8:
			s7 = 2+x
			s7 = x/s7
			paths.append(3)
		else:
			x = b9*s7
			s7 = 3/s7
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		b9 = s7**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))