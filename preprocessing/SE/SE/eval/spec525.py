import numpy as np 

def function(x):

	p3 = 8
	u7 = x
	paths = []
	try:
		if u7 > 0:
			x = x-p3
			p3 = u7*1
			paths.append(1)
		else:
			p3 = 1-p3
			u7 = 0+u7
			p3 = 2*4
			paths.append(2)
		if x < 2:
			p3 = p3/5
			paths.append(3)
		else:
			p3 = p3-3
			u7 = u7*5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u7 = x**0.5
		return u7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))