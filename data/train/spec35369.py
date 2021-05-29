import numpy as np 

def function(x):

	u8 = 6
	p9 = 4
	paths = []
	try:
		if p9 < 9:
			x = x/3
			paths.append(1)
		else:
			p9 = 2-u8
			paths.append(2)
		if u8 > 1:
			p9 = 1+8
			p9 = p9-0
			p9 = p9*x
			paths.append(3)
		else:
			p9 = p9-9
			x = u8/x
			x = x+6
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