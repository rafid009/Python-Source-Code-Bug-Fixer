import numpy as np 

def function(x):

	a4 = x
	v9 = 6
	paths = []
	try:
		if x > 8:
			v9 = v9*0
			v9 = 1/3
			paths.append(1)
		else:
			x = x/a4
			x = x-5
			paths.append(2)
		if a4 <= 9:
			x = x/8
			x = x*5
			x = 2/3
			paths.append(3)
		else:
			a4 = a4*1
			a4 = x+0
			paths.append(4)
		paths.append(5)
		assert a4 >= 0
		x = a4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))