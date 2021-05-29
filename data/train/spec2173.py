import numpy as np 

def function(x):

	a1 = x
	i4 = x
	paths = []
	try:
		if i4 > 9:
			i4 = 1-i4
			paths.append(1)
		else:
			i4 = a1*i4
			a1 = 3-a1
			paths.append(2)
		if a1 <= 8:
			i4 = 1*i4
			paths.append(3)
		else:
			a1 = a1+3
			i4 = 2-0
			i4 = 2*i4
			paths.append(4)
		paths.append(5)
		assert a1 >= 0
		x = a1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))