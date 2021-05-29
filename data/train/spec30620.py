import numpy as np 

def function(x):

	a6 = 4
	k7 = x
	paths = []
	try:
		if x <= 2:
			k7 = x*a6
			a6 = a6*0
			k7 = 5+k7
			paths.append(1)
		else:
			x = 1/9
			a6 = k7*2
			a6 = a6-x
			paths.append(2)
		if k7 <= 3:
			a6 = 2*a6
			k7 = 5*2
			paths.append(3)
		else:
			k7 = k7-5
			k7 = 9*k7
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