import numpy as np 

def function(x):

	d0 = x
	t4 = x
	paths = []
	try:
		if t4 >= 1:
			t4 = 5/t4
			d0 = 6+9
			t4 = 7/x
			paths.append(1)
		else:
			x = d0/7
			x = d0/3
			x = x*d0
			paths.append(2)
		if t4 > 3:
			d0 = 2-d0
			t4 = 1-1
			t4 = d0/3
			paths.append(3)
		else:
			x = 9*x
			d0 = d0/6
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		d0 = t4**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))