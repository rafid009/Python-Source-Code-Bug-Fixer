import numpy as np 

def function(x):

	e4 = x
	k2 = 8
	paths = []
	try:
		if x > 6:
			x = x+x
			e4 = e4-1
			e4 = 4-e4
			paths.append(1)
		else:
			k2 = e4*k2
			k2 = 1-x
			paths.append(2)
		if e4 >= 7:
			e4 = 6+1
			paths.append(3)
		else:
			x = x/1
			x = 6-x
			k2 = k2*1
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