import numpy as np 

def function(x):

	b0 = 9
	d5 = x
	paths = []
	try:
		if x <= 3:
			b0 = 6*d5
			b0 = 5/b0
			paths.append(1)
		else:
			d5 = d5-3
			d5 = d5*4
			paths.append(2)
		if b0 >= 9:
			x = b0+d5
			b0 = 3+b0
			b0 = b0/1
			paths.append(3)
		else:
			x = 6+x
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