import numpy as np 

def function(x):

	b3 = x
	e4 = 8
	paths = []
	try:
		if b3 > 9:
			e4 = e4*x
			e4 = 5-e4
			paths.append(1)
		else:
			x = 8+b3
			paths.append(2)
		if b3 <= 8:
			x = x/9
			paths.append(3)
		else:
			e4 = e4/3
			x = b3*0
			b3 = 8-b3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))