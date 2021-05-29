import numpy as np 

def function(x):

	t1 = 3
	v8 = x
	paths = []
	try:
		if v8 <= 1:
			x = x/5
			t1 = x/x
			paths.append(1)
		else:
			t1 = t1/1
			v8 = 7+0
			t1 = 1+t1
			paths.append(2)
		if v8 < 7:
			v8 = 0-0
			t1 = v8-t1
			t1 = 2*4
			paths.append(3)
		else:
			v8 = t1+x
			x = x/8
			x = x*7
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