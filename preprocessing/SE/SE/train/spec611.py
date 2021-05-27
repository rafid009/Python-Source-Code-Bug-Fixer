import numpy as np 

def function(x):

	j5 = x
	k3 = x
	paths = []
	try:
		if k3 <= 4:
			j5 = j5+6
			paths.append(1)
		else:
			j5 = x+j5
			j5 = 0+j5
			paths.append(2)
		if x >= 4:
			x = x+5
			x = 9*5
			paths.append(3)
		else:
			x = x-0
			paths.append(4)
		paths.append(5)
		assert k3 >= 0
		x = k3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))