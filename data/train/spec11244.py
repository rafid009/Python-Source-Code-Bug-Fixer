import numpy as np 

def function(x):

	a9 = x
	b7 = x
	paths = []
	try:
		if x < 8:
			x = a9-2
			paths.append(1)
		else:
			x = 6+x
			paths.append(2)
		if a9 <= 9:
			x = 6+x
			paths.append(3)
		else:
			a9 = b7*2
			x = b7-x
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