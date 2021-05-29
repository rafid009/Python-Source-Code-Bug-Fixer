import numpy as np 

def function(x):

	p1 = 8
	u8 = x
	paths = []
	try:
		if u8 < 1:
			u8 = u8+1
			paths.append(1)
		else:
			p1 = 6-u8
			u8 = u8/u8
			x = x+9
			paths.append(2)
		if p1 > 3:
			u8 = 0/u8
			paths.append(3)
		else:
			p1 = p1-4
			u8 = u8+x
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