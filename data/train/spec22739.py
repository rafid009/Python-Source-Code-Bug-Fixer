import numpy as np 

def function(x):

	b5 = 2
	e3 = x
	paths = []
	try:
		if b5 <= 7:
			x = 6*x
			e3 = x+e3
			b5 = e3-b5
			paths.append(1)
		else:
			b5 = e3+2
			paths.append(2)
		if e3 > 0:
			x = x/e3
			e3 = 6-e3
			x = 2/1
			paths.append(3)
		else:
			b5 = e3+b5
			paths.append(4)
		paths.append(5)
		assert e3 >= 0
		x = e3**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))