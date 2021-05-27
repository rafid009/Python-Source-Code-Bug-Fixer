import numpy as np 

def function(x):

	d7 = 7
	a8 = x
	paths = []
	try:
		if x < 5:
			a8 = a8-5
			d7 = d7+a8
			a8 = 7*a8
			paths.append(1)
		else:
			d7 = d7-5
			a8 = a8/4
			x = x-7
			paths.append(2)
		if x > 9:
			x = x+3
			x = x+9
			x = 9*0
			paths.append(3)
		else:
			d7 = 5+x
			x = 7-x
			a8 = a8/x
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