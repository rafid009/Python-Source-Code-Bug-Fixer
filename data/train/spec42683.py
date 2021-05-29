import numpy as np 

def function(x):

	a7 = 9
	d3 = x
	paths = []
	try:
		if x > 9:
			a7 = 7+a7
			a7 = d3*a7
			a7 = a7-4
			paths.append(1)
		else:
			a7 = a7+d3
			paths.append(2)
		if d3 <= 9:
			x = x*0
			a7 = a7+9
			paths.append(3)
		else:
			d3 = d3*6
			x = x+4
			paths.append(4)
		paths.append(5)
		assert a7 >= 0
		a7 = a7**0.5
		return a7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))