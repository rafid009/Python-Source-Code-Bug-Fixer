import numpy as np 

def function(x):

	s9 = x
	j1 = x
	paths = []
	try:
		if s9 >= 9:
			j1 = s9*j1
			j1 = x/j1
			paths.append(1)
		else:
			x = x-1
			x = x-7
			x = s9-x
			paths.append(2)
		if j1 > 7:
			s9 = 1+1
			s9 = 9-s9
			s9 = j1*1
			paths.append(3)
		else:
			s9 = s9-7
			j1 = j1+j1
			x = 7*x
			paths.append(4)
		paths.append(5)
		assert s9 >= 0
		s9 = s9**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))