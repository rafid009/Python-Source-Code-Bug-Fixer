import numpy as np 

def function(x):

	v5 = x
	e1 = x
	x = 8
	paths = []
	try:
		if v5 <= 5:
			x = 0*x
			paths.append(1)
		else:
			x = x/e1
			x = x+x
			paths.append(2)
		if x > 1:
			v5 = v5+5
			paths.append(3)
		else:
			v5 = v5+e1
			paths.append(4)
		paths.append(5)
		assert e1 >= 0
		x = e1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))