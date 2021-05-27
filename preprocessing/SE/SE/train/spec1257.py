import numpy as np 

def function(x):

	a4 = 5
	i4 = x
	paths = []
	try:
		if x > 9:
			x = 6+x
			a4 = a4*8
			paths.append(1)
		else:
			a4 = i4*6
			i4 = 7+i4
			a4 = i4+i4
			paths.append(2)
		if a4 >= 1:
			i4 = i4+0
			x = 7/x
			paths.append(3)
		else:
			i4 = i4*0
			i4 = 4/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		a4 = x**0.5
		return a4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))