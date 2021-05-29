import numpy as np 

def function(x):

	t4 = x
	d9 = x
	paths = []
	try:
		if t4 < 1:
			d9 = d9-2
			x = t4+x
			paths.append(1)
		else:
			x = x*t4
			t4 = 0+t4
			paths.append(2)
		if d9 <= 0:
			d9 = d9+3
			paths.append(3)
		else:
			t4 = t4+3
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		d9 = t4**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))