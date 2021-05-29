import numpy as np 

def function(x):

	a5 = x
	a2 = x
	x = x
	paths = []
	try:
		if a5 > 1:
			x = x*a2
			a5 = a5/a2
			a2 = a2+0
			paths.append(1)
		else:
			a5 = a5/4
			x = x+7
			paths.append(2)
		if x > 1:
			a5 = a5-x
			a5 = a5*7
			x = a5*1
			paths.append(3)
		else:
			a5 = 7*a5
			paths.append(4)
		paths.append(5)
		assert a2 >= 0
		a2 = a2**0.5
		return a2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))