import numpy as np 

def function(x):

	n2 = 5
	b8 = x
	paths = []
	try:
		if x <= 1:
			x = 4-9
			n2 = 7+n2
			paths.append(1)
		else:
			b8 = b8/n2
			n2 = x*7
			paths.append(2)
		if b8 <= 3:
			n2 = x*x
			x = 5/x
			x = b8-x
			paths.append(3)
		else:
			n2 = 9-n2
			n2 = n2*1
			b8 = b8+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b8 = x**0.5
		return b8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))