import numpy as np 

def function(x):

	o7 = 2
	e3 = 4
	paths = []
	try:
		if o7 <= 4:
			x = 8+e3
			x = 2-7
			e3 = e3/9
			paths.append(1)
		else:
			x = 8*2
			x = 6-6
			paths.append(2)
		if x <= 4:
			e3 = e3+5
			paths.append(3)
		else:
			e3 = e3*0
			e3 = e3*x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		e3 = x**0.5
		return e3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))