import numpy as np 

def function(x):

	b7 = 7
	k9 = 3
	paths = []
	try:
		if k9 < 5:
			x = x+2
			b7 = 2/b7
			paths.append(1)
		else:
			x = 4-x
			b7 = k9*x
			paths.append(2)
		if k9 <= 5:
			k9 = k9/k9
			k9 = 1+k9
			b7 = b7-6
			paths.append(3)
		else:
			x = x*x
			x = b7+3
			b7 = 5*8
			paths.append(4)
		paths.append(5)
		assert b7 >= 0
		x = b7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))