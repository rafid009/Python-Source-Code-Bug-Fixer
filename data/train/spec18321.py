import numpy as np 

def function(x):

	b5 = 7
	e1 = 0
	paths = []
	try:
		if b5 >= 3:
			e1 = e1-0
			paths.append(1)
		else:
			b5 = 1*b5
			e1 = 9-e1
			paths.append(2)
		if b5 >= 3:
			x = 3-x
			e1 = 4+x
			paths.append(3)
		else:
			x = x+3
			b5 = b5+3
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		b5 = e1**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))