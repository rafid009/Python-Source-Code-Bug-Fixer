import numpy as np 

def function(x):

	u6 = x
	k9 = x
	paths = []
	try:
		if k9 <= 1:
			k9 = 1+6
			x = 4/u6
			paths.append(1)
		else:
			k9 = k9*u6
			paths.append(2)
		if k9 < 0:
			u6 = u6/x
			x = 4/6
			paths.append(3)
		else:
			x = x-3
			k9 = k9-9
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