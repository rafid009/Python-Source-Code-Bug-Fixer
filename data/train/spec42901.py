import numpy as np 

def function(x):

	s4 = x
	e1 = 8
	paths = []
	try:
		if x > 4:
			x = 3-x
			paths.append(1)
		else:
			e1 = s4+e1
			paths.append(2)
		if s4 >= 6:
			e1 = s4+x
			paths.append(3)
		else:
			s4 = 6+s4
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))