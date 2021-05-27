import numpy as np 

def function(x):

	a0 = x
	p6 = 8
	paths = []
	try:
		if p6 > 9:
			x = 8-x
			x = 6*0
			paths.append(1)
		else:
			a0 = a0+6
			a0 = x/6
			paths.append(2)
		if x > 3:
			a0 = 4/a0
			x = 7/a0
			paths.append(3)
		else:
			p6 = x-1
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		a0 = a0**0.5
		return a0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))