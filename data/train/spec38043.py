import numpy as np 

def function(x):

	k9 = x
	n8 = x
	paths = []
	try:
		if k9 <= 9:
			k9 = 5/k9
			paths.append(1)
		else:
			x = 8*x
			n8 = k9+0
			paths.append(2)
		if x <= 7:
			x = 9+x
			paths.append(3)
		else:
			k9 = 8-k9
			k9 = k9-x
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		n8 = k9**0.5
		return n8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))