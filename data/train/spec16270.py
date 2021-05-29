import numpy as np 

def function(x):

	d9 = 5
	a9 = 8
	x = 8
	paths = []
	try:
		if a9 > 6:
			a9 = x+1
			x = d9/1
			x = 5*x
			paths.append(1)
		else:
			x = x/d9
			d9 = a9-a9
			paths.append(2)
		if d9 <= 2:
			x = x/3
			a9 = a9*0
			x = x/4
			paths.append(3)
		else:
			x = 6-d9
			a9 = x+a9
			d9 = 0-7
			paths.append(4)
		paths.append(5)
		assert d9 >= 0
		x = d9**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))