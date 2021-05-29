import numpy as np 

def function(x):

	a6 = x
	b4 = 3
	paths = []
	try:
		if x >= 3:
			a6 = a6-b4
			x = a6+x
			paths.append(1)
		else:
			b4 = b4/2
			paths.append(2)
		if a6 <= 4:
			b4 = b4/7
			x = x+1
			x = x/9
			paths.append(3)
		else:
			x = x+3
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