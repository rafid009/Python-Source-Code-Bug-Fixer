import numpy as np 

def function(x):

	j8 = 8
	k2 = x
	paths = []
	try:
		if k2 <= 4:
			x = x*x
			x = k2*7
			paths.append(1)
		else:
			x = 4+x
			j8 = j8-2
			paths.append(2)
		if j8 >= 1:
			j8 = x*7
			x = 4-k2
			paths.append(3)
		else:
			k2 = 2/k2
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		k2 = k2**0.5
		return k2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))