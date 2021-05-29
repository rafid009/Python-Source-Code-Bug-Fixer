import numpy as np 

def function(x):

	f5 = 1
	s7 = 1
	paths = []
	try:
		if s7 >= 0:
			f5 = 5+1
			s7 = s7*s7
			x = x-2
			paths.append(1)
		else:
			x = x+8
			f5 = 1+x
			paths.append(2)
		if x < 1:
			s7 = x-8
			s7 = 5+s7
			paths.append(3)
		else:
			f5 = 1+f5
			paths.append(4)
		paths.append(5)
		assert s7 >= 0
		x = s7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))