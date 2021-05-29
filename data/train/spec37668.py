import numpy as np 

def function(x):

	q7 = x
	o9 = x
	paths = []
	try:
		if q7 > 1:
			o9 = 4-7
			paths.append(1)
		else:
			q7 = o9/9
			x = 3*2
			paths.append(2)
		if x < 4:
			x = o9-0
			paths.append(3)
		else:
			x = x*1
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