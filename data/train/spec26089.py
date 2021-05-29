import numpy as np 

def function(x):

	k7 = 3
	q7 = 4
	paths = []
	try:
		if x < 5:
			q7 = x*q7
			k7 = 4+3
			x = x+0
			paths.append(1)
		else:
			q7 = x/k7
			q7 = q7/6
			paths.append(2)
		if k7 < 3:
			x = k7*x
			q7 = q7*4
			k7 = x*k7
			paths.append(3)
		else:
			k7 = k7/3
			paths.append(4)
		paths.append(5)
		assert q7 >= 0
		k7 = q7**0.5
		return k7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))