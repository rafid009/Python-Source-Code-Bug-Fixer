import numpy as np 

def function(x):

	a9 = 3
	b9 = x
	paths = []
	try:
		if b9 >= 3:
			x = b9/4
			a9 = a9+4
			a9 = a9+2
			paths.append(1)
		else:
			a9 = a9/3
			x = x/9
			paths.append(2)
		if b9 >= 7:
			a9 = a9+1
			paths.append(3)
		else:
			b9 = a9/b9
			paths.append(4)
		paths.append(5)
		assert b9 >= 0
		x = b9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))