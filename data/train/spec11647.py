import numpy as np 

def function(x):

	k9 = x
	x2 = 6
	paths = []
	try:
		if x >= 7:
			x2 = x2+k9
			k9 = k9+1
			x = 0/k9
			paths.append(1)
		else:
			x = k9/2
			x = x+4
			x2 = x2-7
			paths.append(2)
		if k9 < 5:
			k9 = k9-9
			paths.append(3)
		else:
			x = x*5
			k9 = 2/1
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