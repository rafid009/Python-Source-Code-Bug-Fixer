import numpy as np 

def function(x):

	u8 = 7
	p8 = x
	paths = []
	try:
		if x >= 2:
			u8 = 1*3
			x = x/7
			paths.append(1)
		else:
			u8 = x+1
			p8 = u8*9
			paths.append(2)
		if x > 7:
			x = x*p8
			x = p8*x
			p8 = 8/4
			paths.append(3)
		else:
			p8 = 3*p8
			u8 = u8-3
			paths.append(4)
		paths.append(5)
		assert p8 >= 0
		u8 = p8**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))