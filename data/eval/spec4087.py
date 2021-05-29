import numpy as np 

def function(x):

	j3 = x
	a1 = 5
	paths = []
	try:
		if a1 >= 0:
			x = x-a1
			paths.append(1)
		else:
			a1 = j3/a1
			x = 1-8
			j3 = j3*3
			paths.append(2)
		if j3 <= 7:
			a1 = a1/x
			a1 = a1/3
			paths.append(3)
		else:
			j3 = a1+j3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		j3 = x**0.5
		return j3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))