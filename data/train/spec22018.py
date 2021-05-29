import numpy as np 

def function(x):

	s9 = 9
	j9 = x
	paths = []
	try:
		if s9 >= 6:
			s9 = 3*j9
			paths.append(1)
		else:
			j9 = j9-0
			x = x-9
			s9 = s9/s9
			paths.append(2)
		if j9 > 2:
			s9 = 8-1
			paths.append(3)
		else:
			j9 = 0*9
			x = s9-5
			j9 = j9*s9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j9 = x**0.5
		return j9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))