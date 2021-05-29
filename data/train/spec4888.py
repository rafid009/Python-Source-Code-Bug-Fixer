import numpy as np 

def function(x):

	f6 = 0
	x2 = x
	paths = []
	try:
		if x2 >= 8:
			f6 = f6*f6
			x = x/3
			paths.append(1)
		else:
			x = x+9
			paths.append(2)
		if x >= 5:
			f6 = 3+f6
			x2 = x2+x2
			x = f6+0
			paths.append(3)
		else:
			f6 = f6-8
			paths.append(4)
		paths.append(5)
		assert x2 >= 0
		x2 = x2**0.5
		return x2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))