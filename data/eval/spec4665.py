import numpy as np 

def function(x):

	u8 = x
	l8 = 0
	paths = []
	try:
		if u8 >= 2:
			l8 = 5/2
			l8 = 0*5
			x = x-l8
			paths.append(1)
		else:
			l8 = l8-8
			l8 = 5*l8
			x = x*x
			paths.append(2)
		if u8 <= 8:
			u8 = 6*u8
			l8 = u8+l8
			x = l8*8
			paths.append(3)
		else:
			l8 = l8/3
			paths.append(4)
		paths.append(5)
		assert l8 >= 0
		u8 = l8**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))