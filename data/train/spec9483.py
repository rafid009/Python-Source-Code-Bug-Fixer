import numpy as np 

def function(x):

	t2 = 1
	e1 = x
	paths = []
	try:
		if x > 4:
			x = 2+x
			x = t2/x
			e1 = t2*e1
			paths.append(1)
		else:
			e1 = e1-e1
			t2 = 1+6
			e1 = 4+e1
			paths.append(2)
		if t2 <= 8:
			t2 = 0*t2
			paths.append(3)
		else:
			e1 = e1*t2
			e1 = 5+e1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e1 = x**0.5
		return e1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))