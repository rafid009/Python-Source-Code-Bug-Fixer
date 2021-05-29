import numpy as np 

def function(x):

	s2 = x
	j4 = x
	paths = []
	try:
		if s2 >= 5:
			x = s2+x
			s2 = s2*7
			paths.append(1)
		else:
			s2 = s2+0
			s2 = s2*s2
			paths.append(2)
		if s2 <= 2:
			x = x/5
			x = 9+x
			j4 = 7-j4
			paths.append(3)
		else:
			j4 = 7-s2
			x = x-j4
			paths.append(4)
		paths.append(5)
		assert j4 >= 0
		j4 = j4**0.5
		return j4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))