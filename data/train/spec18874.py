import numpy as np 

def function(x):

	a5 = 9
	k7 = 2
	paths = []
	try:
		if k7 <= 8:
			a5 = a5-7
			a5 = 2/x
			k7 = k7-k7
			paths.append(1)
		else:
			k7 = 9+k7
			paths.append(2)
		if x >= 0:
			a5 = a5+1
			k7 = 8*k7
			a5 = a5+7
			paths.append(3)
		else:
			a5 = 3+a5
			a5 = a5-6
			paths.append(4)
		paths.append(5)
		assert a5 >= 0
		a5 = a5**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))