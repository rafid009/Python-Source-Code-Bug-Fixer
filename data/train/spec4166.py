import numpy as np 

def function(x):

	r8 = 3
	d7 = x
	paths = []
	try:
		if r8 <= 3:
			r8 = 0-9
			d7 = 3/x
			paths.append(1)
		else:
			r8 = r8*2
			x = 7*0
			paths.append(2)
		if x > 9:
			x = 8/x
			d7 = d7-d7
			paths.append(3)
		else:
			r8 = 2*x
			x = x-r8
			d7 = d7*6
			paths.append(4)
		paths.append(5)
		assert d7 >= 0
		d7 = d7**0.5
		return d7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))