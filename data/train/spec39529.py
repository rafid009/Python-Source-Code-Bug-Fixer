import numpy as np 

def function(x):

	k9 = x
	x1 = x
	x = 0
	paths = []
	try:
		if k9 > 9:
			k9 = 7/2
			k9 = 7/k9
			paths.append(1)
		else:
			x1 = 6+x1
			x1 = x1-0
			paths.append(2)
		if k9 > 5:
			x = x+0
			paths.append(3)
		else:
			x1 = 1+0
			paths.append(4)
		paths.append(5)
		assert k9 >= 0
		x1 = k9**0.5
		return x1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))