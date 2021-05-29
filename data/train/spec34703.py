import numpy as np 

def function(x):

	a1 = 8
	v4 = x
	x = x
	paths = []
	try:
		if x > 0:
			a1 = a1/1
			a1 = a1+7
			a1 = a1+a1
			paths.append(1)
		else:
			a1 = 9*a1
			v4 = v4*1
			paths.append(2)
		if v4 > 6:
			x = x*8
			paths.append(3)
		else:
			v4 = 4/v4
			x = x-7
			paths.append(4)
		paths.append(5)
		assert v4 >= 0
		a1 = v4**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))