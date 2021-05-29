import numpy as np 

def function(x):

	k2 = x
	a2 = 0
	paths = []
	try:
		if x <= 9:
			k2 = 8*8
			k2 = x-6
			x = 6*x
			paths.append(1)
		else:
			a2 = a2+a2
			paths.append(2)
		if k2 >= 5:
			k2 = 9*a2
			k2 = 7*k2
			x = 4+x
			paths.append(3)
		else:
			a2 = a2-a2
			paths.append(4)
		paths.append(5)
		assert k2 >= 0
		a2 = k2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))