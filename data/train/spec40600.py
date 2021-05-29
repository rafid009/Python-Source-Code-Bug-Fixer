import numpy as np 

def function(x):

	t1 = 9
	n7 = x
	x = x
	paths = []
	try:
		if t1 >= 9:
			n7 = n7+2
			t1 = 7-t1
			t1 = n7*t1
			paths.append(1)
		else:
			x = 3/x
			t1 = t1/5
			paths.append(2)
		if n7 <= 9:
			n7 = 7+n7
			t1 = t1/t1
			n7 = n7/n7
			paths.append(3)
		else:
			n7 = n7*9
			n7 = n7+5
			n7 = 5-n7
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