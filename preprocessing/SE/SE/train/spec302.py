import numpy as np 

def function(x):

	p8 = x
	u5 = x
	paths = []
	try:
		if p8 < 2:
			p8 = 2*7
			paths.append(1)
		else:
			u5 = 7*7
			paths.append(2)
		if u5 <= 4:
			p8 = p8/u5
			u5 = u5*p8
			paths.append(3)
		else:
			x = 6*8
			x = u5-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		u5 = x**0.5
		return u5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))