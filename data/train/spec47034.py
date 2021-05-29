import numpy as np 

def function(x):

	u2 = x
	k7 = 3
	paths = []
	try:
		if u2 >= 3:
			k7 = 1-x
			x = x+x
			k7 = 9*5
			paths.append(1)
		else:
			k7 = 8/k7
			u2 = x+k7
			paths.append(2)
		if u2 < 6:
			u2 = u2+4
			paths.append(3)
		else:
			k7 = k7*x
			k7 = k7-0
			k7 = 5*2
			paths.append(4)
		paths.append(5)
		assert u2 >= 0
		k7 = u2**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))