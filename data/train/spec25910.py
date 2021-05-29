import numpy as np 

def function(x):

	d4 = 8
	b1 = x
	x = 5
	paths = []
	try:
		if x > 3:
			b1 = b1*3
			d4 = 4-1
			d4 = d4*6
			paths.append(1)
		else:
			b1 = 4+b1
			x = 4+x
			b1 = d4/b1
			paths.append(2)
		if b1 >= 5:
			d4 = d4*1
			x = 1-8
			paths.append(3)
		else:
			b1 = b1+3
			d4 = 8*b1
			x = 9+d4
			paths.append(4)
		paths.append(5)
		assert b1 >= 0
		d4 = b1**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))