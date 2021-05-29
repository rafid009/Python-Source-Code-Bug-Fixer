import numpy as np 

def function(x):

	e8 = 7
	s4 = 1
	paths = []
	try:
		if x < 8:
			s4 = s4-5
			paths.append(1)
		else:
			e8 = 1-e8
			x = 6+x
			x = x/2
			paths.append(2)
		if x <= 8:
			s4 = s4-8
			e8 = 6/e8
			e8 = x-7
			paths.append(3)
		else:
			e8 = e8*s4
			s4 = 1+s4
			paths.append(4)
		paths.append(5)
		assert s4 >= 0
		e8 = s4**0.5
		return e8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))