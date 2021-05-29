import numpy as np 

def function(x):

	o9 = 7
	u7 = 1
	paths = []
	try:
		if x > 4:
			x = o9*4
			x = 8*x
			paths.append(1)
		else:
			u7 = u7*5
			o9 = o9/u7
			paths.append(2)
		if x <= 1:
			x = x/7
			o9 = u7+x
			o9 = o9/x
			paths.append(3)
		else:
			x = 1+u7
			o9 = o9-u7
			u7 = o9-2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		o9 = x**0.5
		return o9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))