import numpy as np 

def function(x):

	b3 = 8
	u6 = x
	x = x
	paths = []
	try:
		if b3 > 7:
			b3 = 1*b3
			u6 = u6+u6
			u6 = u6*5
			paths.append(1)
		else:
			b3 = u6-b3
			paths.append(2)
		if u6 <= 4:
			u6 = 1/u6
			paths.append(3)
		else:
			x = x*7
			u6 = 5+u6
			x = 6*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u6 = x**0.5
		return u6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))