import numpy as np 

def function(x):

	a4 = 3
	o9 = 9
	paths = []
	try:
		if o9 > 0:
			a4 = a4/9
			o9 = o9+5
			x = x+7
			paths.append(1)
		else:
			o9 = o9*3
			paths.append(2)
		if x < 6:
			a4 = 2-6
			o9 = 2-a4
			a4 = a4-6
			paths.append(3)
		else:
			x = x+x
			a4 = 2/a4
			o9 = o9*1
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