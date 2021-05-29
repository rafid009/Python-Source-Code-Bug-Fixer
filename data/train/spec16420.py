import numpy as np 

def function(x):

	k9 = x
	x9 = 8
	paths = []
	try:
		if x <= 3:
			x9 = x9*0
			paths.append(1)
		else:
			x = k9+x
			paths.append(2)
		if x <= 5:
			k9 = k9+5
			paths.append(3)
		else:
			k9 = k9-1
			x9 = 4/7
			k9 = 8-k9
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		x = k9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))