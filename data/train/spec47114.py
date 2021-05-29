import numpy as np 

def function(x):

	k0 = x
	k9 = x
	paths = []
	try:
		if x > 9:
			k9 = 9*2
			k9 = 5+x
			paths.append(1)
		else:
			k9 = 4-k9
			k0 = 5+k9
			k9 = k9+0
			paths.append(2)
		if k0 >= 8:
			k9 = x/k9
			paths.append(3)
		else:
			x = 1+k9
			k0 = 0+4
			k0 = k0+1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k0 = x**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))