import numpy as np 

def function(x):

	d9 = 9
	x0 = 9
	paths = []
	try:
		if d9 > 0:
			d9 = 4+d9
			x = x+7
			paths.append(1)
		else:
			x0 = d9*0
			paths.append(2)
		if x >= 4:
			d9 = d9/x
			paths.append(3)
		else:
			x0 = 9*3
			x = x*5
			x = x+x0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x0 = x**0.5
		return x0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))