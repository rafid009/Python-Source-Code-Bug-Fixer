import numpy as np 

def function(x):

	j9 = 5
	s2 = 9
	x = 3
	paths = []
	try:
		if j9 > 9:
			x = x*5
			s2 = s2*8
			paths.append(1)
		else:
			s2 = s2*3
			s2 = 3*s2
			s2 = s2/5
			paths.append(2)
		if s2 < 6:
			s2 = s2/2
			paths.append(3)
		else:
			j9 = x-7
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