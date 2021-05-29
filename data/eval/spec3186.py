import numpy as np 

def function(x):

	v8 = x
	t1 = 5
	paths = []
	try:
		if x > 1:
			v8 = 5-v8
			t1 = t1*0
			paths.append(1)
		else:
			x = x+8
			t1 = t1/7
			paths.append(2)
		if v8 > 1:
			x = 1/x
			paths.append(3)
		else:
			v8 = x-v8
			x = x+4
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