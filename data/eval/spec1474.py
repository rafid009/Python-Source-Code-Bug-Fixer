import numpy as np 

def function(x):

	j2 = x
	q6 = 4
	paths = []
	try:
		if j2 >= 2:
			x = j2*x
			x = j2-7
			paths.append(1)
		else:
			j2 = x/j2
			paths.append(2)
		if q6 >= 3:
			j2 = j2*j2
			x = 8+x
			paths.append(3)
		else:
			j2 = 2+3
			x = x-0
			j2 = j2*2
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