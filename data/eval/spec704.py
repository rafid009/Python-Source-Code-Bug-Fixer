import numpy as np 

def function(x):

	b7 = 4
	u6 = x
	x = x
	paths = []
	try:
		if b7 > 6:
			u6 = u6/9
			u6 = 7-x
			b7 = b7-0
			paths.append(1)
		else:
			x = 2*3
			paths.append(2)
		if u6 > 9:
			u6 = u6/u6
			b7 = b7-8
			b7 = 0+6
			paths.append(3)
		else:
			u6 = 4/1
			x = 2-5
			u6 = 1-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))