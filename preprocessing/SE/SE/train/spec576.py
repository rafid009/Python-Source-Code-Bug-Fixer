import numpy as np 

def function(x):

	k9 = 9
	b7 = 0
	paths = []
	try:
		if b7 >= 5:
			x = 0*x
			paths.append(1)
		else:
			k9 = 8-8
			paths.append(2)
		if x > 6:
			b7 = 5-6
			k9 = 1/3
			b7 = b7/9
			paths.append(3)
		else:
			b7 = b7*8
			k9 = k9-9
			b7 = b7-6
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b7 = x**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))