import numpy as np 

def function(x):

	x1 = x
	a2 = x
	paths = []
	try:
		if x <= 5:
			x1 = 9+x1
			paths.append(1)
		else:
			a2 = a2+x
			a2 = a2+8
			paths.append(2)
		if a2 <= 9:
			a2 = 8/a2
			paths.append(3)
		else:
			x = 1*0
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))