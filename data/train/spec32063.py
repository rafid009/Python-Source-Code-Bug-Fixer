import numpy as np 

def function(x):

	a8 = x
	j2 = 3
	paths = []
	try:
		if x < 6:
			j2 = x*j2
			x = a8*7
			j2 = j2-2
			paths.append(1)
		else:
			j2 = j2/7
			paths.append(2)
		if j2 >= 8:
			j2 = j2*x
			a8 = 7-4
			paths.append(3)
		else:
			a8 = 6+a8
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		x = a8**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))