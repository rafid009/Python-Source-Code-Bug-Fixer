import numpy as np 

def function(x):

	u6 = x
	b1 = x
	paths = []
	try:
		if b1 > 7:
			b1 = b1/1
			b1 = 1/b1
			paths.append(1)
		else:
			u6 = 1*x
			u6 = u6-3
			b1 = b1-6
			paths.append(2)
		if u6 < 0:
			x = 4-6
			x = 6*x
			paths.append(3)
		else:
			u6 = u6/u6
			x = 0+x
			x = x-8
			paths.append(4)
		paths.append(5)
		assert u6 >= 0
		u6 = u6**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))