import numpy as np 

def function(x):

	u5 = 2
	e6 = 7
	paths = []
	try:
		if e6 < 2:
			u5 = 8+u5
			e6 = e6*7
			paths.append(1)
		else:
			e6 = e6*7
			e6 = e6+1
			u5 = u5/7
			paths.append(2)
		if e6 >= 9:
			e6 = e6/1
			x = x*1
			paths.append(3)
		else:
			e6 = 4/x
			x = 4+x
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