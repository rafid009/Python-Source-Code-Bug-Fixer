import numpy as np 

def function(x):

	o4 = 5
	u8 = 4
	x = x
	paths = []
	try:
		if x < 0:
			u8 = 9+1
			o4 = 2+u8
			paths.append(1)
		else:
			o4 = o4-6
			paths.append(2)
		if o4 >= 4:
			x = x+3
			o4 = 8-x
			o4 = 7*o4
			paths.append(3)
		else:
			x = o4*x
			u8 = 5*8
			paths.append(4)
		paths.append(5)
		assert o4 >= 0
		o4 = o4**0.5
		return o4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))