import numpy as np 

def function(x):

	e3 = x
	s1 = x
	paths = []
	try:
		if e3 > 6:
			x = 9*x
			paths.append(1)
		else:
			x = 8*e3
			paths.append(2)
		if e3 < 4:
			e3 = 5+1
			x = 2-x
			paths.append(3)
		else:
			s1 = 0-0
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		e3 = s1**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))