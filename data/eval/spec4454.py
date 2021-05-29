import numpy as np 

def function(x):

	a3 = x
	b0 = x
	paths = []
	try:
		if x < 9:
			x = 4+x
			b0 = b0-3
			paths.append(1)
		else:
			a3 = b0-5
			a3 = a3+7
			a3 = a3+a3
			paths.append(2)
		if b0 <= 0:
			x = 9+x
			a3 = a3-9
			paths.append(3)
		else:
			b0 = b0/b0
			paths.append(4)
		paths.append(5)
		assert a3 >= 0
		b0 = a3**0.5
		return b0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))