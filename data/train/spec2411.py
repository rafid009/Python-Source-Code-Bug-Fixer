import numpy as np 

def function(x):

	t1 = x
	d5 = 9
	paths = []
	try:
		if x <= 7:
			d5 = t1-4
			d5 = d5-t1
			d5 = 2*d5
			paths.append(1)
		else:
			d5 = 6-5
			d5 = d5-6
			d5 = d5/8
			paths.append(2)
		if t1 >= 5:
			x = x+9
			t1 = 4/d5
			paths.append(3)
		else:
			d5 = x+7
			d5 = d5-d5
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