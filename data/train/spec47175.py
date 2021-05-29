import numpy as np 

def function(x):

	b2 = 9
	u9 = x
	paths = []
	try:
		if u9 > 6:
			b2 = b2-1
			paths.append(1)
		else:
			x = x-9
			b2 = u9*b2
			u9 = 1/b2
			paths.append(2)
		if u9 >= 6:
			x = 6+1
			u9 = 5*7
			u9 = b2+b2
			paths.append(3)
		else:
			u9 = u9/1
			x = 8*x
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