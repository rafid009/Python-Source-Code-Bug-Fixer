import numpy as np 

def function(x):

	t1 = x
	v8 = 5
	paths = []
	try:
		if v8 > 7:
			v8 = t1/1
			t1 = t1*6
			paths.append(1)
		else:
			t1 = t1-4
			v8 = 0+v8
			paths.append(2)
		if t1 >= 4:
			t1 = t1/t1
			t1 = t1/v8
			t1 = t1/4
			paths.append(3)
		else:
			t1 = t1/x
			paths.append(4)
		paths.append(5)
		assert x >= 0
		v8 = x**0.5
		return v8, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))