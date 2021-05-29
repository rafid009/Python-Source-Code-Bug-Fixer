import numpy as np 

def function(x):

	u8 = 4
	b3 = x
	paths = []
	try:
		if b3 < 7:
			u8 = u8*x
			paths.append(1)
		else:
			b3 = x/7
			b3 = 7*b3
			b3 = 4+b3
			paths.append(2)
		if b3 > 8:
			x = 1+x
			u8 = u8/b3
			x = 2+x
			paths.append(3)
		else:
			b3 = b3*u8
			x = x+2
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		x = u8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))