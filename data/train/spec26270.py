import numpy as np 

def function(x):

	b6 = 2
	f1 = 6
	paths = []
	try:
		if x < 4:
			b6 = b6/b6
			x = 3-7
			paths.append(1)
		else:
			f1 = 7+6
			paths.append(2)
		if x < 5:
			b6 = b6+x
			b6 = b6+3
			b6 = b6/3
			paths.append(3)
		else:
			b6 = b6/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f1 = x**0.5
		return f1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))