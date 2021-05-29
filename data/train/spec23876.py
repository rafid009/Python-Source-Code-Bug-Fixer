import numpy as np 

def function(x):

	n2 = 0
	b6 = 9
	x = x
	paths = []
	try:
		if x > 4:
			b6 = 4*9
			n2 = n2+n2
			b6 = 8*x
			paths.append(1)
		else:
			b6 = 4/4
			x = x/7
			paths.append(2)
		if b6 < 2:
			x = x-1
			n2 = n2+7
			x = x-0
			paths.append(3)
		else:
			b6 = 1-7
			b6 = b6-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n2 = x**0.5
		return n2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))