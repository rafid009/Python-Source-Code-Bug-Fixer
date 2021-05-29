import numpy as np 

def function(x):

	a9 = 2
	s2 = x
	x = 4
	paths = []
	try:
		if x < 4:
			x = 5/a9
			s2 = s2-s2
			paths.append(1)
		else:
			a9 = a9+0
			x = a9-5
			x = 6-s2
			paths.append(2)
		if s2 <= 4:
			a9 = a9-6
			a9 = 3-4
			paths.append(3)
		else:
			x = s2/x
			s2 = 0+x
			paths.append(4)
		paths.append(5)
		assert s2 >= 0
		x = s2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))