import numpy as np 

def function(x):

	j8 = x
	a5 = 3
	paths = []
	try:
		if j8 >= 3:
			j8 = 9*2
			paths.append(1)
		else:
			a5 = a5*3
			paths.append(2)
		if j8 > 5:
			a5 = 5/x
			j8 = 4+j8
			a5 = x+2
			paths.append(3)
		else:
			x = 7/x
			a5 = x/a5
			x = x*9
			paths.append(4)
		paths.append(5)
		assert j8 >= 0
		a5 = j8**0.5
		return a5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))