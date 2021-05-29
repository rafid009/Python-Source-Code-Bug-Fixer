import numpy as np 

def function(x):

	j9 = 4
	a2 = x
	paths = []
	try:
		if j9 > 6:
			j9 = j9-7
			j9 = j9-9
			paths.append(1)
		else:
			j9 = j9/a2
			paths.append(2)
		if x >= 3:
			x = 1*2
			x = x/a2
			a2 = 0-a2
			paths.append(3)
		else:
			x = x+3
			a2 = j9-a2
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