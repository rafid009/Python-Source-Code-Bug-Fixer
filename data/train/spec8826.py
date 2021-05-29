import numpy as np 

def function(x):

	k9 = x
	a2 = x
	paths = []
	try:
		if x > 0:
			a2 = 6*4
			paths.append(1)
		else:
			k9 = k9*9
			k9 = k9+a2
			paths.append(2)
		if k9 >= 7:
			a2 = a2/k9
			k9 = k9*k9
			k9 = 4/k9
			paths.append(3)
		else:
			x = 0+3
			a2 = 5/a2
			x = x+9
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		x = a2**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))