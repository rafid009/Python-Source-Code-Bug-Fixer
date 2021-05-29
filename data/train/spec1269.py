import numpy as np 

def function(x):

	t1 = 1
	o6 = 2
	paths = []
	try:
		if x <= 6:
			t1 = 6-6
			paths.append(1)
		else:
			x = x-t1
			x = 2/o6
			x = 8+x
			paths.append(2)
		if x >= 9:
			o6 = o6*t1
			o6 = o6*1
			paths.append(3)
		else:
			o6 = x*0
			o6 = 0+o6
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