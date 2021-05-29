import numpy as np 

def function(x):

	d8 = x
	a8 = x
	paths = []
	try:
		if x <= 9:
			x = x-x
			a8 = 5+d8
			x = x+x
			paths.append(1)
		else:
			d8 = 3*0
			a8 = a8*0
			x = 9*6
			paths.append(2)
		if d8 >= 2:
			d8 = 5-d8
			d8 = d8*8
			paths.append(3)
		else:
			a8 = a8+1
			x = x*9
			a8 = x-4
			paths.append(4)
		paths.append(5)
		assert d8 >= 0
		a8 = d8**0.5
		return a8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))