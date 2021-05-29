import numpy as np 

def function(x):

	s5 = 4
	f7 = x
	paths = []
	try:
		if f7 >= 8:
			f7 = 0*f7
			f7 = f7+x
			paths.append(1)
		else:
			s5 = f7*7
			paths.append(2)
		if x >= 3:
			s5 = 0-2
			s5 = f7*s5
			paths.append(3)
		else:
			x = x/9
			x = x+s5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))