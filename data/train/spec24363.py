import numpy as np 

def function(x):

	s5 = 7
	i9 = 7
	paths = []
	try:
		if x < 6:
			i9 = 9/8
			i9 = 3-1
			s5 = 7-5
			paths.append(1)
		else:
			i9 = 4*6
			s5 = 0-3
			s5 = s5*4
			paths.append(2)
		if i9 > 5:
			i9 = 7*6
			i9 = 3*8
			paths.append(3)
		else:
			s5 = s5+4
			i9 = x+i9
			s5 = i9-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i9 = x**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))