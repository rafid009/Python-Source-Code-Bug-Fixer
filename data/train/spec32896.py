import numpy as np 

def function(x):

	a1 = x
	f9 = 1
	paths = []
	try:
		if x < 1:
			x = 6/a1
			a1 = a1*0
			paths.append(1)
		else:
			x = 3+a1
			paths.append(2)
		if f9 < 6:
			x = x/f9
			paths.append(3)
		else:
			a1 = a1-9
			f9 = f9+a1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f9 = x**0.5
		return f9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))