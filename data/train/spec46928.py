import numpy as np 

def function(x):

	s1 = 2
	f9 = x
	paths = []
	try:
		if s1 <= 8:
			f9 = f9+7
			paths.append(1)
		else:
			f9 = s1-2
			s1 = 0-9
			paths.append(2)
		if s1 >= 3:
			s1 = f9*s1
			f9 = f9/2
			paths.append(3)
		else:
			s1 = s1+6
			paths.append(4)
		paths.append(5)
		assert f9 >= 0
		f9 = f9**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))