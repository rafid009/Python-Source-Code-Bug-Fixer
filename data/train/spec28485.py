import numpy as np 

def function(x):

	s2 = 6
	j5 = 4
	paths = []
	try:
		if x < 3:
			x = 9+x
			s2 = 5*6
			paths.append(1)
		else:
			s2 = s2*9
			x = x*j5
			j5 = 2-1
			paths.append(2)
		if j5 >= 3:
			s2 = s2-2
			paths.append(3)
		else:
			x = j5+2
			j5 = 7-x
			s2 = 8-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))