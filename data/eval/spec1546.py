import numpy as np 

def function(x):

	j9 = 2
	s2 = 5
	paths = []
	try:
		if s2 <= 4:
			j9 = 2*8
			paths.append(1)
		else:
			s2 = 6/s2
			paths.append(2)
		if x < 4:
			s2 = 4*s2
			j9 = 5+x
			s2 = j9+s2
			paths.append(3)
		else:
			x = 6*x
			s2 = s2*5
			s2 = s2-3
			paths.append(4)
		paths.append(5)
		assert j9 >= 0
		x = j9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))