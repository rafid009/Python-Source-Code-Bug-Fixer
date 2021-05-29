import numpy as np 

def function(x):

	f8 = x
	s0 = x
	paths = []
	try:
		if f8 < 4:
			s0 = s0/9
			paths.append(1)
		else:
			x = 9+x
			paths.append(2)
		if f8 >= 7:
			x = x-x
			paths.append(3)
		else:
			f8 = 0*1
			f8 = f8/3
			f8 = 8-f8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f8 = x**0.5
		return f8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))