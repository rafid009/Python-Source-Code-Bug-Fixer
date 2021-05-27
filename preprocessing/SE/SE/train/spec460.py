import numpy as np 

def function(x):

	t4 = 4
	d2 = x
	paths = []
	try:
		if x > 5:
			t4 = t4/7
			t4 = t4-7
			d2 = 3*5
			paths.append(1)
		else:
			x = 9*x
			x = 3*x
			t4 = t4-5
			paths.append(2)
		if x <= 8:
			t4 = 5+t4
			paths.append(3)
		else:
			x = t4+x
			d2 = 1/d2
			paths.append(4)
		paths.append(5)
		assert d2 >= 0
		t4 = d2**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))