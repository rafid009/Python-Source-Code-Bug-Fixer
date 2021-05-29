import numpy as np 

def function(x):

	v2 = 7
	d4 = 7
	paths = []
	try:
		if v2 <= 2:
			d4 = d4/9
			x = 5/3
			paths.append(1)
		else:
			x = 5-v2
			d4 = d4+7
			x = 2/x
			paths.append(2)
		if x < 6:
			d4 = d4*2
			paths.append(3)
		else:
			d4 = 2+d4
			v2 = v2-1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d4 = x**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))