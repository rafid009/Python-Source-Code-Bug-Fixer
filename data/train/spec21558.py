import numpy as np 

def function(x):

	n1 = 5
	b8 = x
	paths = []
	try:
		if n1 < 9:
			n1 = x-n1
			paths.append(1)
		else:
			b8 = 8*0
			n1 = 9-b8
			x = x/4
			paths.append(2)
		if b8 < 3:
			n1 = 0*4
			paths.append(3)
		else:
			b8 = 9-0
			paths.append(4)
		paths.append(5)
		assert b8 >= 0
		n1 = b8**0.5
		return n1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))