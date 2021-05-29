import numpy as np 

def function(x):

	a7 = x
	a0 = 4
	paths = []
	try:
		if x > 1:
			x = 2-x
			a0 = a0*0
			paths.append(1)
		else:
			a7 = 5+a7
			a0 = a0+4
			paths.append(2)
		if a0 <= 0:
			a0 = a0*0
			x = x/1
			paths.append(3)
		else:
			x = 6*9
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