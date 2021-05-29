import numpy as np 

def function(x):

	s8 = x
	f1 = x
	paths = []
	try:
		if s8 <= 7:
			s8 = s8+x
			f1 = 7-f1
			paths.append(1)
		else:
			f1 = x+f1
			x = 0/1
			paths.append(2)
		if f1 < 2:
			s8 = s8*f1
			paths.append(3)
		else:
			x = 7+x
			f1 = f1-f1
			f1 = f1+6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))