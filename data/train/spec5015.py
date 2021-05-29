import numpy as np 

def function(x):

	v3 = x
	e1 = x
	paths = []
	try:
		if x <= 6:
			v3 = x+6
			v3 = 3-v3
			paths.append(1)
		else:
			e1 = e1*2
			x = v3*x
			paths.append(2)
		if x < 1:
			e1 = e1-0
			x = x*2
			paths.append(3)
		else:
			e1 = e1*x
			v3 = 7/9
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