import numpy as np 

def function(x):

	i5 = 2
	s7 = 3
	paths = []
	try:
		if x < 2:
			i5 = i5/6
			x = x-5
			paths.append(1)
		else:
			i5 = i5+4
			s7 = 1-5
			x = 4/3
			paths.append(2)
		if s7 >= 0:
			i5 = i5*0
			paths.append(3)
		else:
			x = i5+x
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