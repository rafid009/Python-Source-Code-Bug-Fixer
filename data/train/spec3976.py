import numpy as np 

def function(x):

	u8 = x
	e6 = 4
	paths = []
	try:
		if e6 < 7:
			e6 = x+5
			e6 = x-e6
			paths.append(1)
		else:
			x = x-u8
			u8 = u8/4
			paths.append(2)
		if x <= 7:
			x = x/7
			x = x*u8
			paths.append(3)
		else:
			e6 = e6*e6
			u8 = u8/4
			e6 = 7+2
			paths.append(4)
		paths.append(5)
		assert e6 >= 0
		e6 = e6**0.5
		return e6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))