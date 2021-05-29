import numpy as np 

def function(x):

	s7 = 5
	p9 = x
	paths = []
	try:
		if x <= 3:
			p9 = p9-4
			paths.append(1)
		else:
			s7 = 8-8
			paths.append(2)
		if s7 <= 8:
			x = x-3
			paths.append(3)
		else:
			p9 = p9*x
			p9 = 5-p9
			paths.append(4)
		paths.append(5)
		assert p9 >= 0
		p9 = p9**0.5
		return p9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))