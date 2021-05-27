import numpy as np 

def function(x):

	k9 = x
	a7 = 2
	paths = []
	try:
		if a7 <= 1:
			x = 1*x
			paths.append(1)
		else:
			k9 = k9-8
			paths.append(2)
		if a7 > 8:
			k9 = 2/k9
			k9 = 7/x
			x = 7*x
			paths.append(3)
		else:
			k9 = k9-1
			k9 = k9+x
			x = 3/5
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