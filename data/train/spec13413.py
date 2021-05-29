import numpy as np 

def function(x):

	l5 = 2
	j3 = 2
	x = x
	paths = []
	try:
		if x >= 0:
			j3 = j3*l5
			j3 = j3/5
			x = x-3
			paths.append(1)
		else:
			x = 7-x
			paths.append(2)
		if l5 >= 3:
			x = x-2
			l5 = l5/6
			paths.append(3)
		else:
			x = x/l5
			l5 = l5*j3
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