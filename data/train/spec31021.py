import numpy as np 

def function(x):

	o5 = 5
	t9 = 2
	paths = []
	try:
		if t9 >= 4:
			o5 = o5/x
			x = x-2
			x = 8*x
			paths.append(1)
		else:
			o5 = o5*2
			paths.append(2)
		if x > 5:
			o5 = 7*3
			x = t9-6
			t9 = 3*x
			paths.append(3)
		else:
			t9 = 0-t9
			x = 5+x
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