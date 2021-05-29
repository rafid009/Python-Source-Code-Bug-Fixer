import numpy as np 

def function(x):

	x5 = x
	s4 = 5
	paths = []
	try:
		if x5 < 5:
			x = 8/4
			s4 = s4+4
			x = x-5
			paths.append(1)
		else:
			x = s4*0
			x = x+5
			paths.append(2)
		if s4 < 2:
			x = x+x
			paths.append(3)
		else:
			s4 = x5+s4
			s4 = s4-x5
			x5 = x5/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x5 = x**0.5
		return x5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))