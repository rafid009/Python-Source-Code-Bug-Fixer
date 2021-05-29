import numpy as np 

def function(x):

	b4 = x
	a9 = 9
	paths = []
	try:
		if x < 9:
			a9 = 1*a9
			x = x/1
			paths.append(1)
		else:
			x = 9+x
			a9 = 8+3
			x = x/9
			paths.append(2)
		if a9 <= 9:
			a9 = 8*a9
			paths.append(3)
		else:
			x = x*2
			paths.append(4)
		paths.append(5)
		assert b4 >= 0
		x = b4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))