import numpy as np 

def function(x):

	p8 = x
	s8 = 3
	paths = []
	try:
		if x <= 8:
			s8 = 6-6
			p8 = p8-9
			paths.append(1)
		else:
			p8 = p8*s8
			s8 = x/6
			paths.append(2)
		if p8 >= 4:
			x = x+p8
			paths.append(3)
		else:
			x = 4*p8
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		s8 = p8**0.5
		return s8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))