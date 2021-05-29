import numpy as np 

def function(x):

	u2 = x
	u8 = 0
	paths = []
	try:
		if x > 3:
			u2 = u2/5
			u8 = u8*0
			x = 8*x
			paths.append(1)
		else:
			u2 = u2-8
			x = x-4
			u8 = x+u8
			paths.append(2)
		if u2 > 9:
			u2 = u2-9
			paths.append(3)
		else:
			x = x+u8
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		u2 = u2**0.5
		return u2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))