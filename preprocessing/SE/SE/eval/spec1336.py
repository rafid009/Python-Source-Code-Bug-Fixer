import numpy as np 

def function(x):

	d3 = 7
	t8 = x
	x = 4
	paths = []
	try:
		if x >= 8:
			d3 = 9*d3
			x = x-t8
			paths.append(1)
		else:
			x = x*1
			paths.append(2)
		if x < 8:
			d3 = d3*3
			x = x*3
			x = t8-9
			paths.append(3)
		else:
			x = d3/x
			t8 = 7*5
			paths.append(4)
		paths.append(5)
		assert t8 >= 0
		t8 = t8**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))