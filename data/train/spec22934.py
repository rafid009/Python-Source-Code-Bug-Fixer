import numpy as np 

def function(x):

	b4 = x
	a9 = x
	paths = []
	try:
		if b4 <= 1:
			b4 = 3*b4
			paths.append(1)
		else:
			x = b4/6
			paths.append(2)
		if b4 < 6:
			b4 = b4/3
			paths.append(3)
		else:
			x = 1-6
			b4 = a9/5
			b4 = 7*b4
			paths.append(4)
		paths.append(5)
		assert a9 >= 0
		a9 = a9**0.5
		return a9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))