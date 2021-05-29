import numpy as np 

def function(x):

	j0 = 6
	s6 = x
	paths = []
	try:
		if x > 8:
			x = x*j0
			j0 = j0/7
			s6 = s6*s6
			paths.append(1)
		else:
			x = x-2
			paths.append(2)
		if s6 >= 6:
			s6 = s6+x
			s6 = 9*s6
			paths.append(3)
		else:
			x = x+s6
			j0 = x-9
			j0 = j0/8
			paths.append(4)
		paths.append(5)
		assert j0 >= 0
		j0 = j0**0.5
		return j0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))