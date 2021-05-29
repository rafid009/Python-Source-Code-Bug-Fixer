import numpy as np 

def function(x):

	y8 = 3
	b0 = x
	paths = []
	try:
		if y8 > 8:
			b0 = b0/6
			y8 = b0*b0
			paths.append(1)
		else:
			y8 = x+y8
			y8 = y8*8
			paths.append(2)
		if x <= 5:
			y8 = b0*0
			paths.append(3)
		else:
			x = x+b0
			b0 = x*x
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