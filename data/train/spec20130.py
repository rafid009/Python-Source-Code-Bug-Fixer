import numpy as np 

def function(x):

	i1 = x
	s1 = x
	paths = []
	try:
		if i1 <= 5:
			s1 = 8/s1
			s1 = s1*6
			paths.append(1)
		else:
			x = 0*5
			paths.append(2)
		if x < 5:
			i1 = 8/i1
			s1 = 5/s1
			s1 = 2+s1
			paths.append(3)
		else:
			x = 9-1
			i1 = i1/x
			paths.append(4)
		paths.append(5)
		assert i1 >= 0
		x = i1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))