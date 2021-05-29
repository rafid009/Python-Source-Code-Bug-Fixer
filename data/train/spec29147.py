import numpy as np 

def function(x):

	p8 = 7
	s8 = 1
	paths = []
	try:
		if x >= 0:
			x = 3+1
			paths.append(1)
		else:
			s8 = x-1
			x = 9+9
			paths.append(2)
		if s8 <= 7:
			s8 = s8+p8
			s8 = s8/x
			p8 = s8-p8
			paths.append(3)
		else:
			p8 = p8/2
			p8 = 7/x
			s8 = s8-6
			paths.append(4)
		paths.append(5)
		assert s8 >= 0
		p8 = s8**0.5
		return p8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))