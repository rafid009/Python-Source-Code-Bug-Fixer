import numpy as np 

def function(x):

	a4 = 2
	b6 = x
	paths = []
	try:
		if x <= 5:
			x = x+6
			b6 = 0-5
			paths.append(1)
		else:
			x = x/1
			a4 = a4+2
			paths.append(2)
		if a4 < 3:
			a4 = a4*b6
			b6 = b6-6
			a4 = x/a4
			paths.append(3)
		else:
			b6 = 6*b6
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		b6 = a4**0.5
		return b6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))