import numpy as np 

def function(x):

	e1 = x
	j8 = x
	x = 4
	paths = []
	try:
		if x < 0:
			x = 4*e1
			e1 = 9*x
			paths.append(1)
		else:
			e1 = 3-2
			x = x*2
			e1 = e1+j8
			paths.append(2)
		if e1 > 0:
			e1 = x/e1
			paths.append(3)
		else:
			j8 = 5*j8
			e1 = j8-e1
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