import numpy as np 

def function(x):

	k1 = x
	e1 = 0
	paths = []
	try:
		if k1 >= 9:
			k1 = k1/3
			e1 = k1-8
			paths.append(1)
		else:
			k1 = 9+5
			x = x*8
			paths.append(2)
		if e1 >= 5:
			x = x*k1
			x = x/x
			paths.append(3)
		else:
			k1 = e1+7
			x = k1-1
			e1 = e1+k1
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		e1 = e1**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))