import numpy as np 

def function(x):

	s8 = x
	i9 = x
	paths = []
	try:
		if x >= 9:
			s8 = s8-4
			paths.append(1)
		else:
			i9 = i9+6
			i9 = x+i9
			i9 = 1*i9
			paths.append(2)
		if x < 2:
			s8 = s8/6
			i9 = 3/i9
			i9 = i9/x
			paths.append(3)
		else:
			i9 = i9*s8
			x = x/9
			x = x*7
			paths.append(4)
		paths.append(5)
		assert i9 >= 0
		i9 = i9**0.5
		return i9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))