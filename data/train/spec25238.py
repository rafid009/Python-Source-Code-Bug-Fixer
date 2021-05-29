import numpy as np 

def function(x):

	n6 = x
	e1 = x
	paths = []
	try:
		if x > 4:
			x = x+9
			paths.append(1)
		else:
			e1 = e1+x
			n6 = n6*x
			paths.append(2)
		if e1 > 3:
			x = n6/5
			paths.append(3)
		else:
			x = 0+0
			x = x/9
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