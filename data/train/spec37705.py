import numpy as np 

def function(x):

	f6 = 6
	s8 = 4
	paths = []
	try:
		if s8 > 4:
			s8 = x/s8
			x = x*1
			paths.append(1)
		else:
			s8 = 8+s8
			x = x+2
			s8 = f6/f6
			paths.append(2)
		if f6 < 6:
			f6 = f6/6
			s8 = 8/2
			x = 6-0
			paths.append(3)
		else:
			f6 = f6*8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f6 = x**0.5
		return f6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))