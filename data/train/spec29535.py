import numpy as np 

def function(x):

	r5 = x
	t1 = 8
	paths = []
	try:
		if x >= 8:
			t1 = t1+1
			paths.append(1)
		else:
			t1 = t1*4
			paths.append(2)
		if x < 0:
			t1 = t1*7
			t1 = 7+x
			r5 = t1/5
			paths.append(3)
		else:
			x = r5/1
			r5 = 6/r5
			paths.append(4)
		paths.append(5)
		assert r5 >= 0
		r5 = r5**0.5
		return r5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))