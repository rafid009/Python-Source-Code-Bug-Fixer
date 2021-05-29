import numpy as np 

def function(x):

	b3 = x
	f1 = 0
	paths = []
	try:
		if x >= 2:
			f1 = 2+8
			f1 = f1*6
			paths.append(1)
		else:
			x = 1-b3
			b3 = b3-f1
			paths.append(2)
		if f1 >= 4:
			f1 = f1+f1
			x = 9-x
			x = f1+x
			paths.append(3)
		else:
			f1 = f1+9
			b3 = b3+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))