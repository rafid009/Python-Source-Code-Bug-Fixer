import numpy as np 

def function(x):

	n1 = x
	b2 = x
	paths = []
	try:
		if x < 5:
			x = x/1
			x = b2+4
			paths.append(1)
		else:
			b2 = x-b2
			paths.append(2)
		if n1 > 6:
			x = x*x
			n1 = b2*4
			paths.append(3)
		else:
			x = 2-x
			b2 = b2+5
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		n1 = n1**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))