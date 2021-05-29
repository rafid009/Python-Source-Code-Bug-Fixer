import numpy as np 

def function(x):

	f2 = 1
	b0 = x
	paths = []
	try:
		if b0 >= 5:
			f2 = f2+0
			x = 2/6
			paths.append(1)
		else:
			x = x/f2
			paths.append(2)
		if f2 >= 9:
			f2 = f2+0
			paths.append(3)
		else:
			x = 3+x
			b0 = f2-3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b0 = x**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))