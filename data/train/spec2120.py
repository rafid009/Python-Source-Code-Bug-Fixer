import numpy as np 

def function(x):

	s9 = 9
	e3 = 6
	paths = []
	try:
		if s9 <= 4:
			s9 = s9+0
			paths.append(1)
		else:
			x = x-s9
			s9 = 8/s9
			paths.append(2)
		if x <= 9:
			e3 = 0-e3
			s9 = 2+s9
			s9 = e3+s9
			paths.append(3)
		else:
			x = 3-e3
			e3 = x-0
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		e3 = s9**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))