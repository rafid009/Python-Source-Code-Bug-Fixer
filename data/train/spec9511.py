import numpy as np 

def function(x):

	i1 = x
	s2 = x
	paths = []
	try:
		if x <= 5:
			s2 = s2-9
			paths.append(1)
		else:
			i1 = i1-6
			i1 = 6/i1
			x = x*1
			paths.append(2)
		if x < 7:
			s2 = s2-i1
			paths.append(3)
		else:
			x = 7/i1
			s2 = s2+4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i1 = x**0.5
		return i1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))