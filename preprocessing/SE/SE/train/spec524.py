import numpy as np 

def function(x):

	s4 = x
	e8 = 5
	paths = []
	try:
		if e8 <= 4:
			e8 = 6-8
			x = 6+2
			paths.append(1)
		else:
			e8 = x-4
			s4 = s4/6
			e8 = e8*9
			paths.append(2)
		if s4 <= 3:
			e8 = s4+6
			paths.append(3)
		else:
			e8 = e8/e8
			paths.append(4)
		paths.append(5)
		assert e8 >= 0
		x = e8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))