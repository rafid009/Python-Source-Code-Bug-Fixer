import numpy as np 

def function(x):

	f1 = x
	a8 = 1
	paths = []
	try:
		if x < 9:
			f1 = f1+8
			x = x-a8
			a8 = x/a8
			paths.append(1)
		else:
			a8 = 6/4
			paths.append(2)
		if f1 > 2:
			a8 = a8+a8
			f1 = x+1
			paths.append(3)
		else:
			x = f1/1
			a8 = a8-0
			f1 = f1-f1
			paths.append(4)
		paths.append(5)
		assert f1 >= 0
		a8 = f1**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))