import numpy as np 

def function(x):

	d2 = 4
	b5 = 6
	paths = []
	try:
		if d2 <= 3:
			x = x*x
			paths.append(1)
		else:
			x = x*7
			d2 = 2-d2
			b5 = b5*x
			paths.append(2)
		if b5 >= 2:
			x = 9-x
			x = x+0
			x = d2-7
			paths.append(3)
		else:
			x = b5/7
			x = x*3
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		d2 = b5**0.5
		return d2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))