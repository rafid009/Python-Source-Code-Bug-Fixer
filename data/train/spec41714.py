import numpy as np 

def function(x):

	s9 = 3
	i5 = x
	paths = []
	try:
		if i5 > 1:
			i5 = i5+x
			paths.append(1)
		else:
			s9 = 3+i5
			paths.append(2)
		if x > 2:
			i5 = 5+i5
			paths.append(3)
		else:
			x = s9/5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))