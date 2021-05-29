import numpy as np 

def function(x):

	d6 = 2
	b5 = x
	paths = []
	try:
		if d6 <= 1:
			b5 = b5/b5
			b5 = 0*4
			paths.append(1)
		else:
			d6 = d6*b5
			paths.append(2)
		if d6 < 3:
			b5 = b5+8
			d6 = 6*9
			x = x/2
			paths.append(3)
		else:
			x = x/d6
			x = b5-x
			b5 = 6*7
			paths.append(4)
		paths.append(5)
		assert b5 >= 0
		b5 = b5**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))