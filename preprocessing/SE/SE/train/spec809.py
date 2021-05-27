import numpy as np 

def function(x):

	b5 = 7
	r9 = x
	paths = []
	try:
		if b5 > 9:
			r9 = r9-9
			r9 = 8+r9
			paths.append(1)
		else:
			x = x+5
			b5 = 4-r9
			paths.append(2)
		if b5 < 3:
			r9 = r9*5
			x = x/8
			r9 = 7*r9
			paths.append(3)
		else:
			b5 = r9-5
			b5 = 6*b5
			x = x-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))