import numpy as np 

def function(x):

	v7 = 3
	u4 = x
	paths = []
	try:
		if v7 >= 1:
			v7 = v7/x
			v7 = v7-u4
			x = x*2
			paths.append(1)
		else:
			x = x+x
			v7 = v7+v7
			x = x+2
			paths.append(2)
		if u4 <= 8:
			x = x+6
			paths.append(3)
		else:
			u4 = u4/3
			x = 4-x
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