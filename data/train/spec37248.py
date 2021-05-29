import numpy as np 

def function(x):

	n8 = x
	b1 = 6
	paths = []
	try:
		if n8 < 5:
			b1 = 5/3
			b1 = b1+5
			paths.append(1)
		else:
			x = 4/6
			n8 = n8+6
			b1 = 7+b1
			paths.append(2)
		if b1 <= 8:
			b1 = b1+8
			b1 = n8-n8
			paths.append(3)
		else:
			b1 = b1-4
			n8 = n8*1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n8 = x**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))