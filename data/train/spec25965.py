import numpy as np 

def function(x):

	u6 = 1
	b0 = x
	paths = []
	try:
		if b0 > 3:
			b0 = b0+6
			paths.append(1)
		else:
			u6 = 1*u6
			x = x-8
			paths.append(2)
		if u6 <= 3:
			b0 = u6*b0
			u6 = u6+u6
			paths.append(3)
		else:
			x = b0/6
			u6 = x/u6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))