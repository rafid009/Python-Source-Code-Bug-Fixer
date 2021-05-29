import numpy as np 

def function(x):

	j8 = 1
	e3 = x
	paths = []
	try:
		if j8 >= 2:
			e3 = e3+9
			x = j8*x
			x = x*2
			paths.append(1)
		else:
			x = 8+x
			paths.append(2)
		if j8 <= 1:
			j8 = j8+0
			e3 = 3-e3
			e3 = e3/2
			paths.append(3)
		else:
			x = e3/9
			x = 2-j8
			x = j8/j8
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