import numpy as np 

def function(x):

	b8 = x
	a6 = x
	x = x
	paths = []
	try:
		if x < 8:
			a6 = a6+1
			b8 = 9/3
			b8 = a6-b8
			paths.append(1)
		else:
			b8 = b8*9
			x = x*x
			x = 4+a6
			paths.append(2)
		if x < 4:
			x = b8*7
			b8 = b8+9
			x = a6+7
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))