import numpy as np 

def function(x):

	t6 = x
	d1 = x
	paths = []
	try:
		if t6 >= 8:
			d1 = 3+d1
			d1 = x-d1
			d1 = 4-4
			paths.append(1)
		else:
			t6 = t6-9
			paths.append(2)
		if x <= 6:
			d1 = d1+d1
			d1 = 5+d1
			x = x*5
			paths.append(3)
		else:
			t6 = 3-d1
			d1 = t6+1
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		x = d1**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))