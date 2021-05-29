import numpy as np 

def function(x):

	p8 = x
	s5 = 7
	paths = []
	try:
		if x <= 9:
			p8 = p8/8
			p8 = p8+3
			x = p8-2
			paths.append(1)
		else:
			s5 = x+x
			p8 = s5+4
			p8 = 2*x
			paths.append(2)
		if p8 <= 9:
			s5 = 3-s5
			p8 = 7/7
			x = 9+x
			paths.append(3)
		else:
			s5 = 6/s5
			x = p8-7
			paths.append(4)
		paths.append(5)
		assert s5 >= 0
		x = s5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))