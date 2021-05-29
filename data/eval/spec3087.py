import numpy as np 

def function(x):

	x4 = 9
	b5 = x
	paths = []
	try:
		if x4 > 2:
			x4 = x4+5
			paths.append(1)
		else:
			x = x-6
			b5 = b5-2
			b5 = 9/7
			paths.append(2)
		if b5 <= 4:
			x = b5+b5
			paths.append(3)
		else:
			x4 = x+b5
			x = x4+x4
			x = 1+1
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