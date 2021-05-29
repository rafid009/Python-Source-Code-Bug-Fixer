import numpy as np 

def function(x):

	p2 = 9
	k9 = x
	paths = []
	try:
		if k9 > 3:
			k9 = k9/1
			p2 = 8/8
			paths.append(1)
		else:
			x = 5/2
			paths.append(2)
		if x >= 1:
			k9 = k9+5
			p2 = 4+3
			paths.append(3)
		else:
			k9 = 5/3
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