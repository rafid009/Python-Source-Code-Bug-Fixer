import numpy as np 

def function(x):

	k9 = x
	y4 = x
	paths = []
	try:
		if y4 < 8:
			x = x-x
			paths.append(1)
		else:
			k9 = x*k9
			paths.append(2)
		if x >= 3:
			k9 = 0-k9
			k9 = k9+k9
			x = 6*k9
			paths.append(3)
		else:
			x = x*y4
			k9 = 5*k9
			k9 = 8/k9
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		k9 = k9**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))