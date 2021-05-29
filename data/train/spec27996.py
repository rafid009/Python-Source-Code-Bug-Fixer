import numpy as np 

def function(x):

	d1 = x
	t2 = 8
	paths = []
	try:
		if d1 < 4:
			x = x-8
			paths.append(1)
		else:
			t2 = 8+d1
			d1 = d1/8
			paths.append(2)
		if x >= 9:
			t2 = t2-2
			x = 7/5
			paths.append(3)
		else:
			d1 = d1-5
			t2 = x*9
			d1 = d1*d1
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		d1 = t2**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))