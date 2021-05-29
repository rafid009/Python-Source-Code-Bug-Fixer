import numpy as np 

def function(x):

	t3 = x
	d9 = x
	paths = []
	try:
		if d9 > 8:
			t3 = t3*t3
			x = 3-4
			paths.append(1)
		else:
			t3 = d9*x
			t3 = t3*5
			t3 = 9+t3
			paths.append(2)
		if t3 >= 6:
			d9 = d9*2
			d9 = 5+d9
			paths.append(3)
		else:
			t3 = t3/d9
			x = x+3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		d9 = x**0.5
		return d9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))