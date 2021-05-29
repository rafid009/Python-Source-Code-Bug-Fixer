import numpy as np 

def function(x):

	b5 = x
	n4 = 8
	paths = []
	try:
		if b5 >= 4:
			n4 = n4/b5
			b5 = 7*1
			paths.append(1)
		else:
			n4 = x/2
			paths.append(2)
		if b5 > 1:
			n4 = n4+1
			b5 = b5/2
			n4 = n4+6
			paths.append(3)
		else:
			n4 = 7/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n4 = x**0.5
		return n4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))