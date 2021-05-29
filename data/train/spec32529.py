import numpy as np 

def function(x):

	e1 = x
	a4 = 5
	x = 5
	paths = []
	try:
		if e1 <= 5:
			a4 = e1/a4
			x = a4+4
			paths.append(1)
		else:
			x = e1-5
			a4 = 3*a4
			e1 = 2-4
			paths.append(2)
		if x >= 6:
			e1 = e1+a4
			x = a4*a4
			a4 = a4/1
			paths.append(3)
		else:
			a4 = a4+1
			e1 = e1*8
			x = x/x
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		a4 = e1**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))