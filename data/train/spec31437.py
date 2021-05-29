import numpy as np 

def function(x):

	d9 = 7
	t9 = 4
	paths = []
	try:
		if x > 8:
			d9 = d9*8
			x = 6/2
			paths.append(1)
		else:
			x = 5-x
			t9 = t9*1
			d9 = d9*3
			paths.append(2)
		if t9 >= 5:
			d9 = d9/2
			d9 = d9+x
			t9 = t9+3
			paths.append(3)
		else:
			t9 = t9/3
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t9 = x**0.5
		return t9, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))