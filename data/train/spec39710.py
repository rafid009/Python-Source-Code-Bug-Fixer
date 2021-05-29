import numpy as np 

def function(x):

	p9 = x
	s7 = 3
	paths = []
	try:
		if x >= 2:
			p9 = p9/3
			p9 = 7-p9
			paths.append(1)
		else:
			x = p9*1
			paths.append(2)
		if x <= 1:
			x = s7/x
			p9 = p9+x
			paths.append(3)
		else:
			x = p9*0
			x = x-2
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s7 = x**0.5
		return s7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))