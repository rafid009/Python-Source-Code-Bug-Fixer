import numpy as np 

def function(x):

	k2 = x
	a2 = x
	paths = []
	try:
		if a2 >= 4:
			x = 8*a2
			a2 = a2+a2
			paths.append(1)
		else:
			k2 = 8*2
			a2 = a2-4
			x = 9+x
			paths.append(2)
		if x < 5:
			x = x*5
			paths.append(3)
		else:
			x = x+9
			x = 4+5
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