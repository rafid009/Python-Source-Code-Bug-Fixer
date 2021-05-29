import numpy as np 

def function(x):

	s9 = x
	i7 = 0
	x = x
	paths = []
	try:
		if i7 >= 6:
			s9 = s9+x
			paths.append(1)
		else:
			i7 = 5/5
			i7 = i7*5
			paths.append(2)
		if s9 < 9:
			i7 = i7*s9
			x = s9-8
			i7 = i7-2
			paths.append(3)
		else:
			s9 = s9/4
			x = s9+7
			paths.append(4)
		paths.append(5)
		assert i7 >= 0
		i7 = i7**0.5
		return i7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))