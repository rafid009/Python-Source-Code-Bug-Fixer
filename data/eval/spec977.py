import numpy as np 

def function(x):

	b9 = x
	a7 = x
	x = 0
	paths = []
	try:
		if a7 <= 3:
			a7 = 1/4
			b9 = b9+5
			paths.append(1)
		else:
			x = 1*x
			paths.append(2)
		if b9 <= 5:
			b9 = 7+b9
			b9 = a7*b9
			b9 = 2*b9
			paths.append(3)
		else:
			x = x*x
			x = 4*b9
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