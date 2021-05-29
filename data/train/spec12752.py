import numpy as np 

def function(x):

	k7 = 6
	a2 = 7
	paths = []
	try:
		if a2 > 2:
			k7 = k7+6
			paths.append(1)
		else:
			k7 = 4/a2
			k7 = k7/2
			paths.append(2)
		if k7 >= 5:
			k7 = 6+k7
			a2 = 6/a2
			k7 = 9/x
			paths.append(3)
		else:
			a2 = 4-a2
			x = 1+9
			x = 4/1
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		k7 = k7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))