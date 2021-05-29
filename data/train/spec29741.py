import numpy as np 

def function(x):

	k9 = x
	y5 = 0
	paths = []
	try:
		if x > 9:
			k9 = k9+k9
			paths.append(1)
		else:
			k9 = 5+k9
			paths.append(2)
		if y5 >= 5:
			k9 = y5*9
			paths.append(3)
		else:
			k9 = 8+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k9 = x**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))