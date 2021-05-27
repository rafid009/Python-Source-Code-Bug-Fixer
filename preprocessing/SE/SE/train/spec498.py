import numpy as np 

def function(x):

	q7 = 0
	k9 = x
	paths = []
	try:
		if k9 >= 9:
			k9 = 1*k9
			q7 = q7+0
			paths.append(1)
		else:
			k9 = 2+k9
			x = k9-x
			x = k9+3
			paths.append(2)
		if k9 >= 5:
			k9 = 7+1
			x = q7-6
			x = 7/x
			paths.append(3)
		else:
			x = x*7
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