import numpy as np 

def function(x):

	t2 = x
	d9 = 9
	paths = []
	try:
		if t2 >= 5:
			d9 = d9-t2
			x = d9*d9
			x = x*x
			paths.append(1)
		else:
			t2 = 3*t2
			t2 = 4/t2
			t2 = d9/6
			paths.append(2)
		if x <= 9:
			t2 = t2+7
			x = 8/x
			t2 = 2-t2
			paths.append(3)
		else:
			x = 4/2
			d9 = d9-t2
			d9 = 9-d9
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		t2 = t2**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))