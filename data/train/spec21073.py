import numpy as np 

def function(x):

	e6 = 8
	b5 = x
	x = x
	paths = []
	try:
		if e6 <= 4:
			b5 = x+8
			e6 = 3/b5
			x = x/e6
			paths.append(1)
		else:
			b5 = 6+x
			x = x+7
			paths.append(2)
		if e6 <= 1:
			x = 1/e6
			x = 8*2
			e6 = x+e6
			paths.append(3)
		else:
			e6 = e6+9
			e6 = 6/2
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