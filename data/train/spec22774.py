import numpy as np 

def function(x):

	i5 = 9
	e2 = 8
	paths = []
	try:
		if x <= 7:
			x = i5*x
			paths.append(1)
		else:
			e2 = 3/e2
			e2 = e2*9
			x = e2-8
			paths.append(2)
		if e2 < 5:
			e2 = 1-e2
			paths.append(3)
		else:
			x = x*0
			i5 = 5+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i5 = x**0.5
		return i5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))