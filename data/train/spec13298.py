import numpy as np 

def function(x):

	k5 = 5
	a7 = x
	paths = []
	try:
		if a7 > 4:
			x = x*0
			k5 = k5+5
			x = x/k5
			paths.append(1)
		else:
			k5 = k5-3
			k5 = 2*k5
			x = 7-k5
			paths.append(2)
		if x > 7:
			a7 = 4-a7
			paths.append(3)
		else:
			k5 = k5/6
			x = x+x
			x = x*x
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		x = a7**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))