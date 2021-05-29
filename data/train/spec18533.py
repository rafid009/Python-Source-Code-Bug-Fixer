import numpy as np 

def function(x):

	d4 = x
	t5 = 4
	paths = []
	try:
		if x < 7:
			d4 = d4-7
			paths.append(1)
		else:
			t5 = t5*6
			x = 5*0
			paths.append(2)
		if x > 7:
			t5 = 2+7
			d4 = d4*6
			d4 = 4+6
			paths.append(3)
		else:
			x = d4/6
			paths.append(4)
		paths.append(5)
		assert d4 >= 0
		x = d4**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))