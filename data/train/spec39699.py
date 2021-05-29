import numpy as np 

def function(x):

	f1 = x
	a8 = x
	paths = []
	try:
		if f1 <= 1:
			x = a8*x
			f1 = f1-8
			paths.append(1)
		else:
			f1 = f1*3
			a8 = a8/8
			paths.append(2)
		if x > 5:
			f1 = f1-3
			paths.append(3)
		else:
			x = a8*1
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