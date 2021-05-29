import numpy as np 

def function(x):

	t1 = 4
	j5 = 2
	paths = []
	try:
		if x < 4:
			t1 = t1-0
			paths.append(1)
		else:
			x = x+2
			paths.append(2)
		if x > 4:
			t1 = 5/t1
			t1 = t1+3
			j5 = j5/6
			paths.append(3)
		else:
			t1 = 8/t1
			j5 = 5+j5
			x = x*t1
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