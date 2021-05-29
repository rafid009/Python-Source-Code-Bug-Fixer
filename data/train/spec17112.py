import numpy as np 

def function(x):

	x5 = 4
	b6 = 6
	x = x
	paths = []
	try:
		if b6 > 7:
			b6 = x5/5
			b6 = b6+2
			paths.append(1)
		else:
			b6 = b6+0
			paths.append(2)
		if b6 >= 5:
			x = x/7
			paths.append(3)
		else:
			x5 = 8-9
			x = x*x5
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))