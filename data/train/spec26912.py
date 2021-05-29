import numpy as np 

def function(x):

	t4 = x
	d4 = 4
	paths = []
	try:
		if x > 1:
			x = x+t4
			x = 2+x
			paths.append(1)
		else:
			d4 = 6*d4
			t4 = x*8
			paths.append(2)
		if d4 > 8:
			t4 = t4-d4
			paths.append(3)
		else:
			t4 = t4-0
			t4 = t4/x
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		d4 = t4**0.5
		return d4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))