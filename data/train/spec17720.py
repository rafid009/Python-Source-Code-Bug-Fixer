import numpy as np 

def function(x):

	p3 = 7
	u5 = x
	paths = []
	try:
		if p3 <= 1:
			u5 = u5-x
			x = 9/2
			paths.append(1)
		else:
			u5 = u5+5
			paths.append(2)
		if p3 <= 5:
			u5 = 1-x
			paths.append(3)
		else:
			x = 8/7
			x = u5-3
			x = 0-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		p3 = x**0.5
		return p3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))