import numpy as np 

def function(x):

	e5 = x
	u9 = x
	paths = []
	try:
		if x >= 9:
			x = 3-5
			u9 = u9+8
			paths.append(1)
		else:
			e5 = e5*1
			paths.append(2)
		if e5 <= 5:
			x = x+x
			paths.append(3)
		else:
			u9 = u9*0
			x = 5/x
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