import numpy as np 

def function(x):

	k9 = 4
	i5 = 9
	x = 5
	paths = []
	try:
		if i5 < 9:
			k9 = 5-k9
			paths.append(1)
		else:
			x = 4-i5
			paths.append(2)
		if k9 > 3:
			i5 = i5+4
			paths.append(3)
		else:
			i5 = i5-x
			i5 = i5*6
			x = 5-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))