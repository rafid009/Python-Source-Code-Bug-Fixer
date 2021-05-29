import numpy as np 

def function(x):

	a1 = 3
	k9 = x
	paths = []
	try:
		if a1 > 1:
			k9 = k9-0
			paths.append(1)
		else:
			k9 = 4-x
			k9 = k9+k9
			paths.append(2)
		if a1 > 0:
			x = a1+1
			a1 = 0-a1
			k9 = 2*k9
			paths.append(3)
		else:
			x = x*6
			k9 = 7+k9
			x = a1-5
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		k9 = a1**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))