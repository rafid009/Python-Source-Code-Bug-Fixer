import numpy as np 

def function(x):

	k9 = x
	x6 = 7
	paths = []
	try:
		if k9 < 6:
			x = 8*k9
			x = x*6
			paths.append(1)
		else:
			k9 = k9+x6
			x6 = x/x6
			k9 = x*k9
			paths.append(2)
		if x > 6:
			k9 = k9*8
			x6 = 7+x6
			paths.append(3)
		else:
			x6 = 6*x
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		k9 = k9**0.5
		return k9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))