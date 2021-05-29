import numpy as np 

def function(x):

	g1 = x
	u8 = x
	paths = []
	try:
		if u8 < 5:
			g1 = u8+u8
			g1 = 6*g1
			paths.append(1)
		else:
			g1 = g1-2
			paths.append(2)
		if g1 > 5:
			u8 = g1*5
			x = u8-4
			paths.append(3)
		else:
			g1 = g1+0
			u8 = u8-8
			u8 = 4+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u8 = x**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))