import numpy as np 

def function(x):

	b9 = x
	b0 = 4
	paths = []
	try:
		if b0 > 9:
			x = b9/b9
			paths.append(1)
		else:
			b0 = b0*0
			paths.append(2)
		if b9 < 2:
			b0 = 6+b0
			b0 = b0-8
			b0 = 2*b0
			paths.append(3)
		else:
			x = 1*x
			b9 = 5-1
			x = x*7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))