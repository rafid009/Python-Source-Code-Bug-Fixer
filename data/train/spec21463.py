import numpy as np 

def function(x):

	u8 = x
	p3 = x
	paths = []
	try:
		if u8 < 5:
			p3 = p3*7
			p3 = p3/8
			paths.append(1)
		else:
			x = 0+x
			paths.append(2)
		if u8 <= 9:
			x = x*1
			p3 = 9+9
			x = 8*x
			paths.append(3)
		else:
			x = 5/x
			u8 = u8/8
			x = x/8
			paths.append(4)
		paths.append(5)
		assert u8 >= 0
		u8 = u8**0.5
		return u8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))