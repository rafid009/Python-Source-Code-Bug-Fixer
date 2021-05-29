import numpy as np 

def function(x):

	r4 = 2
	k9 = x
	paths = []
	try:
		if r4 >= 2:
			k9 = k9-k9
			r4 = r4-3
			paths.append(1)
		else:
			x = k9*x
			r4 = x*2
			x = x-9
			paths.append(2)
		if r4 >= 8:
			x = 4*x
			k9 = 6*7
			paths.append(3)
		else:
			x = 3/5
			paths.append(4)
		paths.append(5)
		assert r4 >= 0
		k9 = r4**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))