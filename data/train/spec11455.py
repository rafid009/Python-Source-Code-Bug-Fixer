import numpy as np 

def function(x):

	u4 = 7
	r7 = x
	paths = []
	try:
		if x >= 5:
			u4 = u4*2
			paths.append(1)
		else:
			u4 = 9-x
			x = 5+r7
			u4 = 6-7
			paths.append(2)
		if x < 9:
			x = r7*8
			x = x*3
			paths.append(3)
		else:
			u4 = 5+4
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