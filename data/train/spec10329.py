import numpy as np 

def function(x):

	f9 = 5
	a1 = x
	x = x
	paths = []
	try:
		if a1 < 2:
			x = x/2
			paths.append(1)
		else:
			f9 = a1/7
			a1 = 2-a1
			x = 2/9
			paths.append(2)
		if f9 >= 1:
			x = 9+x
			x = 1+x
			paths.append(3)
		else:
			a1 = 5*x
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