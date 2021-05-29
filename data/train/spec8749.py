import numpy as np 

def function(x):

	r8 = 1
	u4 = x
	paths = []
	try:
		if r8 >= 9:
			r8 = u4/r8
			u4 = x+6
			paths.append(1)
		else:
			x = x*8
			paths.append(2)
		if u4 < 5:
			u4 = u4+u4
			r8 = r8*7
			paths.append(3)
		else:
			x = 0/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u4 = x**0.5
		return u4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))