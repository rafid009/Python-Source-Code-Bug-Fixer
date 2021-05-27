import numpy as np 

def function(x):

	i1 = 2
	a4 = x
	paths = []
	try:
		if i1 >= 7:
			a4 = i1/x
			x = a4/5
			paths.append(1)
		else:
			a4 = i1*9
			x = 2-7
			paths.append(2)
		if i1 > 7:
			a4 = a4-4
			x = x*0
			a4 = a4+i1
			paths.append(3)
		else:
			i1 = i1-2
			a4 = 6-i1
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