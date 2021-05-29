import numpy as np 

def function(x):

	u6 = 7
	l1 = x
	paths = []
	try:
		if u6 > 2:
			x = x+l1
			l1 = l1/7
			paths.append(1)
		else:
			u6 = l1-2
			paths.append(2)
		if u6 <= 5:
			l1 = 7+l1
			u6 = 2/4
			u6 = 0+x
			paths.append(3)
		else:
			u6 = 6-8
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