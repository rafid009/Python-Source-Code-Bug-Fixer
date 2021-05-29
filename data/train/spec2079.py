import numpy as np 

def function(x):

	k9 = x
	x5 = 4
	paths = []
	try:
		if x <= 8:
			x = 7+5
			x5 = x5-0
			paths.append(1)
		else:
			x = x-4
			paths.append(2)
		if x > 8:
			x5 = 7-x5
			paths.append(3)
		else:
			k9 = k9-1
			k9 = 8-k9
			x = 4+x5
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		x = k9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))