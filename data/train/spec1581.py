import numpy as np 

def function(x):

	d8 = x
	u3 = 4
	paths = []
	try:
		if x >= 4:
			d8 = x-0
			x = 8-x
			paths.append(1)
		else:
			d8 = u3*5
			x = 2+x
			u3 = x+u3
			paths.append(2)
		if d8 > 9:
			u3 = u3*2
			u3 = x-5
			paths.append(3)
		else:
			d8 = 8-2
			x = x+0
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