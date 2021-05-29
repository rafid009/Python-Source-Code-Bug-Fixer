import numpy as np 

def function(x):

	k9 = 6
	k4 = x
	paths = []
	try:
		if x <= 6:
			k9 = k9*3
			k9 = 6+k9
			paths.append(1)
		else:
			x = x+0
			k4 = 2*8
			paths.append(2)
		if k9 < 8:
			k4 = k4-k4
			k9 = 2+2
			paths.append(3)
		else:
			k4 = 7-k4
			x = 2-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		k4 = x**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))