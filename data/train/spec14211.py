import numpy as np 

def function(x):

	t7 = 5
	d1 = x
	paths = []
	try:
		if d1 >= 2:
			x = 2-2
			d1 = d1*7
			paths.append(1)
		else:
			x = x/x
			x = 7/7
			x = x/t7
			paths.append(2)
		if x >= 5:
			x = 2+d1
			t7 = t7*9
			paths.append(3)
		else:
			x = d1+4
			paths.append(4)
		paths.append(5)
		assert d1 >= 0
		d1 = d1**0.5
		return d1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))