import numpy as np 

def function(x):

	g1 = 9
	k7 = x
	paths = []
	try:
		if x > 0:
			k7 = 3+8
			x = x/9
			paths.append(1)
		else:
			g1 = g1+k7
			paths.append(2)
		if k7 <= 0:
			k7 = k7-2
			paths.append(3)
		else:
			x = x+4
			paths.append(4)
		paths.append(5)
		assert g1 >= 0
		k7 = g1**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))