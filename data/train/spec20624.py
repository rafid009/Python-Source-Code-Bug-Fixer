import numpy as np 

def function(x):

	b3 = x
	a9 = 3
	paths = []
	try:
		if x <= 5:
			a9 = a9/b3
			b3 = b3+4
			paths.append(1)
		else:
			b3 = b3/1
			a9 = 4+a9
			b3 = b3/b3
			paths.append(2)
		if x > 1:
			b3 = 6*0
			b3 = 7-x
			paths.append(3)
		else:
			x = 1+x
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