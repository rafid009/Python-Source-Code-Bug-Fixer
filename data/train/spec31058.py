import numpy as np 

def function(x):

	d3 = x
	t1 = x
	x = 4
	paths = []
	try:
		if d3 < 3:
			x = t1+t1
			t1 = 1/t1
			paths.append(1)
		else:
			t1 = t1+3
			paths.append(2)
		if d3 >= 4:
			t1 = t1*2
			paths.append(3)
		else:
			d3 = d3/d3
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		d3 = t1**0.5
		return d3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))