import numpy as np 

def function(x):

	b5 = 5
	a2 = 0
	paths = []
	try:
		if x <= 0:
			a2 = x-5
			paths.append(1)
		else:
			b5 = a2/5
			paths.append(2)
		if x > 2:
			a2 = a2-4
			a2 = 7+1
			a2 = a2*a2
			paths.append(3)
		else:
			b5 = b5+0
			paths.append(4)
		paths.append(5)
		assert x >= 0
		b5 = x**0.5
		return b5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))