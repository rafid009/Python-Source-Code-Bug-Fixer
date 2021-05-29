import numpy as np 

def function(x):

	b1 = 8
	d0 = 4
	paths = []
	try:
		if x <= 7:
			x = d0+x
			b1 = 8-1
			d0 = b1*0
			paths.append(1)
		else:
			d0 = 7-d0
			b1 = b1/b1
			d0 = 9*7
			paths.append(2)
		if d0 > 3:
			b1 = b1*6
			paths.append(3)
		else:
			b1 = 6+b1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b1 = x**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))