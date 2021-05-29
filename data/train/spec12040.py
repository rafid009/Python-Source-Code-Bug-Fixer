import numpy as np 

def function(x):

	e5 = x
	v5 = 2
	paths = []
	try:
		if e5 < 2:
			x = v5*x
			e5 = e5*8
			v5 = v5+7
			paths.append(1)
		else:
			v5 = 5-v5
			x = x/6
			x = x+x
			paths.append(2)
		if x > 1:
			e5 = 8/e5
			v5 = v5*6
			e5 = 3*0
			paths.append(3)
		else:
			e5 = x/2
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))