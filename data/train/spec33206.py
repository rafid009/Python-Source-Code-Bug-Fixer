import numpy as np 

def function(x):

	e2 = 5
	k7 = x
	x = x
	paths = []
	try:
		if k7 > 4:
			x = x/6
			x = x*2
			e2 = k7*e2
			paths.append(1)
		else:
			k7 = e2-3
			paths.append(2)
		if e2 >= 8:
			e2 = 9/e2
			x = x-3
			k7 = 8-k7
			paths.append(3)
		else:
			x = e2+0
			e2 = e2/7
			paths.append(4)
		paths.append(5)
		assert k7 >= 0
		e2 = k7**0.5
		return e2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))