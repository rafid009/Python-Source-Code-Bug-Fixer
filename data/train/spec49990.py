import numpy as np 

def function(x):

	s4 = x
	f4 = x
	paths = []
	try:
		if f4 <= 7:
			s4 = s4-5
			s4 = 6*s4
			f4 = 3-f4
			paths.append(1)
		else:
			s4 = s4-5
			x = 5-9
			f4 = s4*4
			paths.append(2)
		if f4 <= 1:
			x = x/3
			s4 = s4+8
			f4 = 3*f4
			paths.append(3)
		else:
			f4 = f4/f4
			f4 = x-f4
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))