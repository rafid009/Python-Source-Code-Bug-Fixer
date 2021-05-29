import numpy as np 

def function(x):

	f2 = 6
	b1 = 3
	paths = []
	try:
		if x < 8:
			f2 = f2+5
			paths.append(1)
		else:
			b1 = b1*b1
			b1 = b1*b1
			f2 = 5/f2
			paths.append(2)
		if f2 < 7:
			f2 = f2/f2
			paths.append(3)
		else:
			f2 = b1+2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b1 = x**0.5
		return b1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))