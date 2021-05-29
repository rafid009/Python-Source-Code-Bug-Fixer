import numpy as np 

def function(x):

	j1 = 6
	s5 = x
	paths = []
	try:
		if j1 <= 4:
			x = 8-x
			s5 = s5*j1
			s5 = s5/6
			paths.append(1)
		else:
			j1 = j1+s5
			paths.append(2)
		if x >= 0:
			x = x+x
			j1 = s5-2
			x = x-3
			paths.append(3)
		else:
			s5 = x+s5
			x = 1-x
			s5 = j1-s5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s5 = x**0.5
		return s5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))