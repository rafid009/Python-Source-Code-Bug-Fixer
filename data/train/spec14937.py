import numpy as np 

def function(x):

	t6 = x
	o1 = x
	paths = []
	try:
		if o1 <= 7:
			o1 = 4-x
			paths.append(1)
		else:
			x = 6/8
			o1 = o1+t6
			x = x+6
			paths.append(2)
		if o1 <= 7:
			x = x*o1
			t6 = t6+o1
			paths.append(3)
		else:
			o1 = 2+o1
			x = x/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t6 = x**0.5
		return t6, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))