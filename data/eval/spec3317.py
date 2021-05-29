import numpy as np 

def function(x):

	s8 = 6
	p9 = x
	paths = []
	try:
		if x >= 5:
			p9 = s8+p9
			paths.append(1)
		else:
			p9 = 8+p9
			paths.append(2)
		if s8 <= 0:
			s8 = 7+s8
			p9 = 4*3
			paths.append(3)
		else:
			p9 = p9-p9
			p9 = x+p9
			s8 = 1-s8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p9 = x**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))