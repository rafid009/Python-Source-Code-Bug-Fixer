import numpy as np 

def function(x):

	o5 = 8
	t1 = x
	paths = []
	try:
		if t1 < 4:
			o5 = o5/t1
			paths.append(1)
		else:
			x = x/t1
			paths.append(2)
		if o5 <= 4:
			t1 = 7*t1
			x = o5-x
			paths.append(3)
		else:
			x = 8*8
			o5 = x+2
			x = 8-x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t1 = x**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))