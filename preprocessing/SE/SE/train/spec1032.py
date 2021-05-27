import numpy as np 

def function(x):

	t2 = 5
	m1 = x
	paths = []
	try:
		if m1 >= 9:
			x = 9-x
			paths.append(1)
		else:
			t2 = 5*t2
			t2 = x/9
			t2 = m1*9
			paths.append(2)
		if t2 >= 0:
			x = x*3
			paths.append(3)
		else:
			t2 = 2/9
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))