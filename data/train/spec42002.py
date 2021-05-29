import numpy as np 

def function(x):

	t8 = 9
	o4 = x
	x = 7
	paths = []
	try:
		if o4 <= 8:
			o4 = 5*o4
			t8 = 3*3
			o4 = 2*o4
			paths.append(1)
		else:
			o4 = o4/6
			paths.append(2)
		if t8 < 8:
			o4 = t8*o4
			x = x-t8
			paths.append(3)
		else:
			t8 = t8*o4
			o4 = o4+7
			x = x-8
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t8 = x**0.5
		return t8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))