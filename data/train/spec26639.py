import numpy as np 

def function(x):

	k9 = 4
	n4 = 5
	paths = []
	try:
		if x <= 1:
			k9 = k9*9
			k9 = x/k9
			paths.append(1)
		else:
			x = k9-3
			x = x-1
			n4 = n4-9
			paths.append(2)
		if n4 < 8:
			n4 = n4-0
			k9 = k9/n4
			paths.append(3)
		else:
			x = n4+0
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