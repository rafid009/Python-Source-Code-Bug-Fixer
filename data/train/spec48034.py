import numpy as np 

def function(x):

	v8 = 4
	u8 = 2
	paths = []
	try:
		if x <= 1:
			v8 = 9+9
			x = x*2
			u8 = 1+x
			paths.append(1)
		else:
			v8 = u8/2
			v8 = v8*x
			v8 = u8/v8
			paths.append(2)
		if v8 > 1:
			v8 = u8-v8
			paths.append(3)
		else:
			u8 = u8-1
			u8 = u8*u8
			x = x+3
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