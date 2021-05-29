import numpy as np 

def function(x):

	a2 = x
	a8 = x
	paths = []
	try:
		if a8 >= 5:
			a2 = 2*0
			x = 3-x
			a8 = 1+a8
			paths.append(1)
		else:
			a8 = a8+3
			x = x*5
			paths.append(2)
		if a8 > 3:
			a2 = a2-4
			a2 = a8/a2
			a8 = a8+1
			paths.append(3)
		else:
			x = x-8
			a2 = x-5
			x = x*7
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		a8 = a8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))