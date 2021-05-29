import numpy as np 

def function(x):

	f4 = x
	v7 = x
	paths = []
	try:
		if x >= 2:
			v7 = v7*v7
			v7 = 9-v7
			f4 = x-f4
			paths.append(1)
		else:
			x = 9/v7
			f4 = v7*5
			v7 = x*7
			paths.append(2)
		if f4 >= 4:
			f4 = f4*0
			x = x+x
			paths.append(3)
		else:
			f4 = f4-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))