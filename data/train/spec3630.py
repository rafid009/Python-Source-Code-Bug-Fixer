import numpy as np 

def function(x):

	p8 = x
	t1 = 8
	paths = []
	try:
		if p8 >= 1:
			p8 = p8*x
			x = 4-x
			paths.append(1)
		else:
			x = p8/x
			t1 = t1*3
			p8 = p8/7
			paths.append(2)
		if x > 6:
			t1 = t1*p8
			x = p8+x
			paths.append(3)
		else:
			p8 = 4-p8
			t1 = 1-t1
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