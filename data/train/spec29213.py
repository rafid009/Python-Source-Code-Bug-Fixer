import numpy as np 

def function(x):

	a1 = 1
	k0 = x
	paths = []
	try:
		if x > 5:
			a1 = a1+a1
			k0 = k0/9
			x = 3+x
			paths.append(1)
		else:
			a1 = 4-a1
			paths.append(2)
		if a1 >= 4:
			a1 = 4/a1
			x = 1*x
			paths.append(3)
		else:
			x = x+x
			paths.append(4)
		paths.append(5)
		assert k0 >= 0
		k0 = k0**0.5
		return k0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))