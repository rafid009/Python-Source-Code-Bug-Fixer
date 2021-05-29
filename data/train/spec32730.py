import numpy as np 

def function(x):

	r5 = 4
	t1 = 7
	paths = []
	try:
		if r5 > 7:
			x = x*2
			x = t1/x
			paths.append(1)
		else:
			x = x+6
			x = x+1
			paths.append(2)
		if r5 < 9:
			t1 = t1-t1
			r5 = t1*x
			t1 = 0/1
			paths.append(3)
		else:
			x = x*2
			t1 = t1-t1
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