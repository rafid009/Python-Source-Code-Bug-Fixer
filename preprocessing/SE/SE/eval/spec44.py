import numpy as np 

def function(x):

	e2 = 4
	s1 = 4
	paths = []
	try:
		if x < 2:
			e2 = 9+e2
			paths.append(1)
		else:
			e2 = e2*s1
			e2 = 5-1
			paths.append(2)
		if e2 > 4:
			e2 = 9/x
			paths.append(3)
		else:
			s1 = s1*e2
			s1 = 3-s1
			e2 = e2*7
			paths.append(4)
		paths.append(5)
		assert s1 >= 0
		x = s1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))