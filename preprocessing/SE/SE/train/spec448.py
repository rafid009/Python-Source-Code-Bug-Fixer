import numpy as np 

def function(x):

	s8 = 6
	f7 = x
	x = x
	paths = []
	try:
		if x < 8:
			f7 = f7-s8
			paths.append(1)
		else:
			s8 = 6+x
			f7 = 0*4
			f7 = f7-f7
			paths.append(2)
		if x < 7:
			f7 = f7*s8
			x = x+x
			x = 2-x
			paths.append(3)
		else:
			s8 = s8-3
			f7 = f7-s8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f7 = x**0.5
		return f7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))