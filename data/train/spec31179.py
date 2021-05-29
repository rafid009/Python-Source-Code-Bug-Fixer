import numpy as np 

def function(x):

	b3 = x
	n2 = 2
	paths = []
	try:
		if x >= 4:
			n2 = n2*0
			b3 = 1-b3
			paths.append(1)
		else:
			n2 = 0/b3
			paths.append(2)
		if x <= 4:
			b3 = b3*b3
			b3 = b3/x
			b3 = b3-7
			paths.append(3)
		else:
			n2 = n2+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b3 = x**0.5
		return b3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))