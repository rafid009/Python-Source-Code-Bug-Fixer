import numpy as np 

def function(x):

	b5 = 1
	r7 = 1
	paths = []
	try:
		if x >= 0:
			r7 = r7*3
			x = x-6
			paths.append(1)
		else:
			r7 = r7+8
			paths.append(2)
		if r7 > 1:
			r7 = r7*1
			paths.append(3)
		else:
			x = r7*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))