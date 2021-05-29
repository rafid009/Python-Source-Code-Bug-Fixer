import numpy as np 

def function(x):

	r7 = 0
	b6 = x
	paths = []
	try:
		if r7 >= 0:
			x = r7-8
			x = 2*8
			x = 7-x
			paths.append(1)
		else:
			x = 9*7
			b6 = 3+x
			paths.append(2)
		if r7 < 3:
			x = 1/x
			b6 = b6+8
			paths.append(3)
		else:
			b6 = 5+b6
			r7 = r7+6
			r7 = r7-7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b6 = x**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))