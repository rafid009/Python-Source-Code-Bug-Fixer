import numpy as np 

def function(x):

	a1 = 9
	i4 = x
	paths = []
	try:
		if i4 > 6:
			a1 = a1*7
			paths.append(1)
		else:
			a1 = i4/5
			a1 = 5-a1
			paths.append(2)
		if x > 7:
			i4 = i4+x
			a1 = a1+a1
			paths.append(3)
		else:
			x = x/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		i4 = x**0.5
		return i4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))