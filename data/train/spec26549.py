import numpy as np 

def function(x):

	k9 = x
	i5 = x
	paths = []
	try:
		if x < 1:
			x = x+0
			paths.append(1)
		else:
			i5 = 3-i5
			i5 = 6+i5
			paths.append(2)
		if x > 3:
			x = 1*x
			k9 = 6*k9
			paths.append(3)
		else:
			i5 = k9+0
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