import numpy as np 

def function(x):

	d1 = x
	k9 = x
	paths = []
	try:
		if x < 4:
			k9 = d1-k9
			d1 = x-9
			paths.append(1)
		else:
			x = x/x
			k9 = x*6
			x = d1+6
			paths.append(2)
		if x >= 0:
			d1 = 9/d1
			k9 = k9*d1
			k9 = 5+4
			paths.append(3)
		else:
			x = x/x
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		k9 = d1**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))