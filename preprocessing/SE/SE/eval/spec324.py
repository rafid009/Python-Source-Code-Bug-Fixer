import numpy as np 

def function(x):

	u4 = x
	n3 = x
	paths = []
	try:
		if n3 > 4:
			n3 = n3/4
			paths.append(1)
		else:
			x = 7/8
			x = u4-2
			n3 = n3+0
			paths.append(2)
		if u4 <= 8:
			u4 = 0/u4
			n3 = n3*9
			paths.append(3)
		else:
			n3 = 0+2
			n3 = n3/5
			n3 = n3/u4
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