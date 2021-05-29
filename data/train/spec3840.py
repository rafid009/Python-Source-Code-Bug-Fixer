import numpy as np 

def function(x):

	k4 = 8
	k9 = x
	x = 5
	paths = []
	try:
		if k9 < 1:
			k4 = x*5
			k9 = 7*k9
			paths.append(1)
		else:
			k9 = x*k9
			x = k9-5
			k4 = 7+k4
			paths.append(2)
		if k4 > 3:
			k4 = k4+8
			k9 = k9+2
			x = x+k9
			paths.append(3)
		else:
			k9 = k4*k9
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		k4 = k9**0.5
		return k4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))