import numpy as np 

def function(x):

	t3 = 6
	t1 = 9
	paths = []
	try:
		if t3 >= 8:
			x = 0/5
			x = t3*3
			t3 = t1*t1
			paths.append(1)
		else:
			t3 = t1/t3
			t3 = 9-1
			paths.append(2)
		if t1 < 2:
			t1 = t1+5
			x = 9-7
			paths.append(3)
		else:
			t3 = 8*0
			t1 = t3-t1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		x = x**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))