import numpy as np 

def function(x):

	t1 = x
	y0 = 4
	paths = []
	try:
		if x < 6:
			t1 = t1+0
			t1 = t1-7
			x = x/2
			paths.append(1)
		else:
			y0 = y0/x
			x = x/6
			paths.append(2)
		if t1 >= 5:
			y0 = x-4
			x = 8*t1
			x = x/y0
			paths.append(3)
		else:
			x = 2+x
			x = 3+x
			x = 5+1
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		t1 = t1**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))