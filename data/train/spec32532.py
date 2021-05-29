import numpy as np 

def function(x):

	f8 = x
	s1 = 9
	paths = []
	try:
		if x >= 0:
			s1 = 1/x
			paths.append(1)
		else:
			x = s1+x
			f8 = f8/7
			paths.append(2)
		if f8 >= 4:
			f8 = f8*5
			x = x-2
			paths.append(3)
		else:
			x = x+5
			s1 = s1-4
			x = x/7
			paths.append(4)
		paths.append(5)
		assert f8 >= 0
		s1 = f8**0.5
		return s1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))