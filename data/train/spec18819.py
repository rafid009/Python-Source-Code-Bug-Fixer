import numpy as np 

def function(x):

	j4 = 0
	e3 = x
	paths = []
	try:
		if e3 <= 5:
			e3 = 6*x
			j4 = e3/e3
			paths.append(1)
		else:
			e3 = 8/9
			j4 = j4-j4
			j4 = j4/x
			paths.append(2)
		if e3 >= 6:
			e3 = e3*1
			x = 4+x
			j4 = 6*2
			paths.append(3)
		else:
			j4 = j4-x
			x = x*4
			x = 4/j4
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