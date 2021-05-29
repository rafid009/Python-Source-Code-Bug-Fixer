import numpy as np 

def function(x):

	p3 = x
	u8 = x
	paths = []
	try:
		if p3 > 9:
			p3 = 3/6
			paths.append(1)
		else:
			u8 = u8*5
			p3 = 8+p3
			u8 = u8*6
			paths.append(2)
		if x < 0:
			x = x-4
			p3 = 5*p3
			x = x+5
			paths.append(3)
		else:
			u8 = 9-u8
			x = 0+2
			paths.append(4)
		paths.append(5)
		assert p3 >= 0
		u8 = p3**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))