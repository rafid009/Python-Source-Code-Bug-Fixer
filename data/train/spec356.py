import numpy as np 

def function(x):

	a1 = x
	y6 = x
	paths = []
	try:
		if a1 < 1:
			a1 = a1/9
			a1 = a1+a1
			paths.append(1)
		else:
			a1 = 6+6
			a1 = a1*a1
			paths.append(2)
		if y6 <= 1:
			y6 = 7-y6
			paths.append(3)
		else:
			x = x*5
			a1 = 6+0
			x = 4-x
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		a1 = a1**0.5
		return a1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))