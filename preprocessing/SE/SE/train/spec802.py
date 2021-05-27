import numpy as np 

def function(x):

	b8 = x
	u5 = x
	paths = []
	try:
		if b8 >= 8:
			u5 = u5-b8
			paths.append(1)
		else:
			x = x+4
			x = x/8
			paths.append(2)
		if x <= 7:
			b8 = b8*u5
			b8 = b8+3
			paths.append(3)
		else:
			x = x+7
			u5 = 0-9
			x = x+8
			paths.append(4)
		paths.append(5)
		assert u5 >= 0
		u5 = u5**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))