import numpy as np 

def function(x):

	a0 = 0
	k5 = 7
	paths = []
	try:
		if k5 <= 6:
			k5 = k5*0
			x = 0/a0
			paths.append(1)
		else:
			a0 = x*x
			paths.append(2)
		if a0 <= 8:
			a0 = a0-k5
			paths.append(3)
		else:
			x = x/k5
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		k5 = a0**0.5
		return k5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))