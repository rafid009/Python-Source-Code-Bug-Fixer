import numpy as np 

def function(x):

	d5 = 2
	t6 = x
	paths = []
	try:
		if t6 >= 9:
			t6 = 2-t6
			d5 = d5/1
			x = x/d5
			paths.append(1)
		else:
			d5 = d5-d5
			t6 = 7*x
			d5 = t6-2
			paths.append(2)
		if x >= 4:
			d5 = 5/d5
			t6 = d5*1
			d5 = d5+9
			paths.append(3)
		else:
			x = d5*1
			d5 = 9*d5
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		d5 = t6**0.5
		return d5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))