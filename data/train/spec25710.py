import numpy as np 

def function(x):

	s4 = 2
	p8 = x
	paths = []
	try:
		if x >= 5:
			s4 = s4-7
			x = 7*x
			paths.append(1)
		else:
			x = x/9
			p8 = p8-x
			s4 = x+9
			paths.append(2)
		if p8 < 1:
			p8 = p8+1
			paths.append(3)
		else:
			s4 = x/p8
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		s4 = p8**0.5
		return s4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))