import numpy as np 

def function(x):

	x7 = 5
	b9 = 5
	paths = []
	try:
		if x7 < 3:
			x = x+9
			x7 = x*x7
			x7 = x7*9
			paths.append(1)
		else:
			x = x7-7
			paths.append(2)
		if x < 8:
			b9 = b9/1
			paths.append(3)
		else:
			x7 = 0+x7
			b9 = x7/b9
			x7 = x7+b9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b9 = x**0.5
		return b9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))