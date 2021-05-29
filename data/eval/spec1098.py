import numpy as np 

def function(x):

	q4 = 5
	u8 = x
	paths = []
	try:
		if q4 > 7:
			u8 = u8/7
			paths.append(1)
		else:
			x = q4*6
			x = 5*x
			x = x*3
			paths.append(2)
		if u8 <= 2:
			x = x/u8
			q4 = 4/q4
			paths.append(3)
		else:
			q4 = q4*9
			u8 = u8/8
			u8 = u8*u8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		q4 = x**0.5
		return q4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))