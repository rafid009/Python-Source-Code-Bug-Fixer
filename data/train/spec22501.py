import numpy as np 

def function(x):

	f1 = 6
	b5 = x
	paths = []
	try:
		if x >= 1:
			x = x/b5
			paths.append(1)
		else:
			f1 = f1+b5
			paths.append(2)
		if f1 > 3:
			f1 = f1+f1
			f1 = b5*f1
			x = b5+4
			paths.append(3)
		else:
			x = 4/f1
			b5 = 9+x
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