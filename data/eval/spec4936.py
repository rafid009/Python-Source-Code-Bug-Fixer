import numpy as np 

def function(x):

	e0 = x
	f4 = x
	x = 8
	paths = []
	try:
		if f4 >= 5:
			e0 = e0/f4
			x = x*2
			x = x/4
			paths.append(1)
		else:
			e0 = 0/6
			x = 0-x
			x = e0/9
			paths.append(2)
		if f4 > 7:
			x = x-7
			e0 = 4/e0
			paths.append(3)
		else:
			f4 = 0*f4
			x = 7+x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		f4 = x**0.5
		return f4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))