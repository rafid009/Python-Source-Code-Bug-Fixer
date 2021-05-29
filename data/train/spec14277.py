import numpy as np 

def function(x):

	q4 = x
	a8 = 6
	paths = []
	try:
		if q4 > 4:
			x = x/3
			x = 9*x
			q4 = q4/2
			paths.append(1)
		else:
			a8 = q4*a8
			x = 6+x
			a8 = x*1
			paths.append(2)
		if a8 > 8:
			x = x+x
			paths.append(3)
		else:
			q4 = 7/1
			a8 = a8-7
			paths.append(4)
		paths.append(5)
		assert a8 >= 0
		a8 = a8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))