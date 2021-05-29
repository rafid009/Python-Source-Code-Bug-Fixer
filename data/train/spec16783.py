import numpy as np 

def function(x):

	b7 = x
	n3 = 1
	paths = []
	try:
		if n3 > 9:
			x = x-4
			x = b7*2
			paths.append(1)
		else:
			n3 = n3+7
			x = x/2
			n3 = 1-n3
			paths.append(2)
		if b7 >= 5:
			n3 = n3+5
			n3 = 1-6
			x = x/4
			paths.append(3)
		else:
			x = 2+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n3 = x**0.5
		return n3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))