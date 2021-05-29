import numpy as np 

def function(x):

	t3 = 6
	d9 = x
	paths = []
	try:
		if x < 1:
			x = x+3
			t3 = 8-t3
			paths.append(1)
		else:
			d9 = 8*d9
			x = 1*x
			t3 = d9/9
			paths.append(2)
		if t3 > 6:
			d9 = d9-8
			d9 = d9-t3
			t3 = t3+4
			paths.append(3)
		else:
			d9 = t3+d9
			t3 = d9/7
			d9 = x+d9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t3 = x**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))