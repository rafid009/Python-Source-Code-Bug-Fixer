import numpy as np 

def function(x):

	f1 = x
	b8 = 9
	x = 6
	paths = []
	try:
		if b8 >= 7:
			x = f1/3
			paths.append(1)
		else:
			b8 = 3/x
			x = 5+3
			f1 = 2/f1
			paths.append(2)
		if b8 > 0:
			f1 = 4*f1
			paths.append(3)
		else:
			b8 = 3/b8
			f1 = 6-f1
			x = x/x
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		x = f1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))