import numpy as np 

def function(x):

	f2 = x
	a1 = x
	x = 2
	paths = []
	try:
		if f2 >= 7:
			f2 = 6+f2
			x = x*3
			f2 = a1-f2
			paths.append(1)
		else:
			a1 = 9-f2
			paths.append(2)
		if x >= 6:
			f2 = f2+8
			x = x*f2
			paths.append(3)
		else:
			a1 = a1+2
			a1 = 0-1
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))