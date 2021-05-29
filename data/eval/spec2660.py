import numpy as np 

def function(x):

	k7 = x
	e1 = x
	paths = []
	try:
		if e1 <= 5:
			k7 = 6+k7
			x = 7-x
			k7 = 8*8
			paths.append(1)
		else:
			x = 4-x
			k7 = k7/4
			x = x+6
			paths.append(2)
		if k7 < 7:
			k7 = e1-k7
			e1 = k7/e1
			paths.append(3)
		else:
			k7 = e1/x
			e1 = k7*e1
			k7 = e1/8
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		x = k7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))