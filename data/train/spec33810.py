import numpy as np 

def function(x):

	v0 = 9
	u8 = x
	paths = []
	try:
		if x > 4:
			u8 = 1*v0
			paths.append(1)
		else:
			v0 = v0*8
			u8 = 4/8
			paths.append(2)
		if u8 < 8:
			u8 = 2*u8
			x = x/6
			u8 = 2+v0
			paths.append(3)
		else:
			u8 = 8/8
			u8 = u8/4
			x = x+5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v0 = x**0.5
		return v0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))