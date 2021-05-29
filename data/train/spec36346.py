import numpy as np 

def function(x):

	t3 = x
	d4 = x
	paths = []
	try:
		if t3 >= 1:
			d4 = d4/4
			paths.append(1)
		else:
			x = x*x
			x = x-2
			paths.append(2)
		if d4 < 8:
			t3 = d4*7
			d4 = 8/5
			paths.append(3)
		else:
			x = 7-x
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		t3 = t3**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))