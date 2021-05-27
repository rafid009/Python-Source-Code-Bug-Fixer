import numpy as np 

def function(x):

	k4 = x
	k9 = x
	paths = []
	try:
		if k9 >= 7:
			x = x+0
			x = 8*x
			k4 = x-k4
			paths.append(1)
		else:
			x = x*x
			paths.append(2)
		if x < 1:
			x = 1+x
			paths.append(3)
		else:
			k4 = 0+k9
			k4 = 1+k4
			k9 = k4-k9
			paths.append(4)
		paths.append(5)
		assert k4 >= 0
		k9 = k4**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))