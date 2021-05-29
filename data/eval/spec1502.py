import numpy as np 

def function(x):

	s9 = 4
	f8 = x
	paths = []
	try:
		if f8 > 1:
			x = x-6
			s9 = 2+s9
			paths.append(1)
		else:
			s9 = f8-2
			x = x+5
			s9 = 1/3
			paths.append(2)
		if x < 5:
			f8 = 6-s9
			x = x+1
			x = x-9
			paths.append(3)
		else:
			s9 = s9+7
			f8 = 9*x
			x = x*s9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		s9 = x**0.5
		return s9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))