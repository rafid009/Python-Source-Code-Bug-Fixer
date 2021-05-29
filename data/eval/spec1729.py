import numpy as np 

def function(x):

	a2 = x
	k9 = 0
	paths = []
	try:
		if k9 >= 9:
			x = 8*x
			k9 = 1/4
			x = 8*9
			paths.append(1)
		else:
			x = 2-1
			x = 8+4
			paths.append(2)
		if k9 > 3:
			k9 = k9/9
			paths.append(3)
		else:
			x = x+5
			k9 = 7-a2
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