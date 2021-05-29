import numpy as np 

def function(x):

	p7 = x
	f8 = 6
	paths = []
	try:
		if x > 5:
			f8 = f8+p7
			p7 = p7*p7
			x = x-7
			paths.append(1)
		else:
			x = p7-3
			p7 = p7*1
			paths.append(2)
		if p7 > 0:
			x = f8+8
			p7 = 6+p7
			f8 = f8*p7
			paths.append(3)
		else:
			f8 = x/f8
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