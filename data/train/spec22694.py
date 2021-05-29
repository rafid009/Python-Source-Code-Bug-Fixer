import numpy as np 

def function(x):

	v3 = 6
	d2 = x
	paths = []
	try:
		if x < 9:
			v3 = 5-v3
			paths.append(1)
		else:
			v3 = v3+4
			d2 = d2-v3
			x = x+9
			paths.append(2)
		if v3 >= 5:
			v3 = 6+v3
			v3 = v3-9
			paths.append(3)
		else:
			v3 = v3/5
			d2 = 0+d2
			v3 = 7*v3
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