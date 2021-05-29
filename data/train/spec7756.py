import numpy as np 

def function(x):

	b7 = x
	a9 = 3
	paths = []
	try:
		if a9 >= 6:
			a9 = 5/a9
			paths.append(1)
		else:
			a9 = a9+0
			a9 = 7/a9
			a9 = 1-a9
			paths.append(2)
		if b7 <= 1:
			a9 = a9*7
			a9 = 6+a9
			paths.append(3)
		else:
			x = x+a9
			x = x*4
			a9 = 4/b7
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		b7 = a9**0.5
		return b7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))