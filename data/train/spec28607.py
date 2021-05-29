import numpy as np 

def function(x):

	k9 = 8
	l9 = 3
	paths = []
	try:
		if l9 > 2:
			l9 = l9/3
			paths.append(1)
		else:
			x = 5-4
			k9 = 7-k9
			paths.append(2)
		if k9 <= 2:
			k9 = 3*k9
			l9 = 5-l9
			k9 = l9-k9
			paths.append(3)
		else:
			x = k9/x
			k9 = 4+5
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