import numpy as np 

def function(x):

	e3 = x
	j5 = x
	paths = []
	try:
		if e3 < 4:
			x = x-2
			e3 = e3+e3
			paths.append(1)
		else:
			j5 = x/x
			j5 = 1+j5
			paths.append(2)
		if j5 < 5:
			x = x*1
			paths.append(3)
		else:
			x = j5/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j5 = x**0.5
		return j5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))