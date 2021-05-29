import numpy as np 

def function(x):

	b6 = 4
	a0 = x
	paths = []
	try:
		if b6 > 3:
			b6 = b6-a0
			b6 = a0-3
			a0 = a0+0
			paths.append(1)
		else:
			a0 = 4/5
			paths.append(2)
		if x <= 0:
			b6 = b6/6
			a0 = 3*1
			a0 = a0*b6
			paths.append(3)
		else:
			x = a0+5
			a0 = 2/6
			x = x/9
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