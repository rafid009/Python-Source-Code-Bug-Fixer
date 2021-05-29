import numpy as np 

def function(x):

	d0 = x
	t5 = 1
	paths = []
	try:
		if x <= 4:
			t5 = 4+t5
			t5 = t5+9
			x = 3-x
			paths.append(1)
		else:
			x = 1/5
			x = 1/2
			paths.append(2)
		if x >= 3:
			t5 = 0-d0
			x = x*1
			t5 = x*t5
			paths.append(3)
		else:
			t5 = t5+7
			paths.append(4)
		paths.append(5)
		assert d0 >= 0
		d0 = d0**0.5
		return d0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))