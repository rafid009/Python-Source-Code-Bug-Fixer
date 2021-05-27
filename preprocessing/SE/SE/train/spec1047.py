import numpy as np 

def function(x):

	w3 = 9
	k7 = x
	paths = []
	try:
		if x >= 6:
			w3 = w3*4
			k7 = 3-5
			x = k7+k7
			paths.append(1)
		else:
			w3 = 6+9
			paths.append(2)
		if k7 < 7:
			x = x+7
			k7 = k7+4
			x = 1+6
			paths.append(3)
		else:
			k7 = k7*5
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		k7 = k7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))