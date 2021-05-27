import numpy as np 

def function(x):

	p6 = 5
	f9 = 2
	paths = []
	try:
		if f9 <= 9:
			x = x+f9
			x = 4/x
			paths.append(1)
		else:
			p6 = p6/4
			paths.append(2)
		if f9 <= 9:
			f9 = f9/p6
			paths.append(3)
		else:
			f9 = 1*0
			f9 = 2*5
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