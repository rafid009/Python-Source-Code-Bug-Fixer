import numpy as np 

def function(x):

	n1 = 1
	t1 = x
	paths = []
	try:
		if x > 8:
			n1 = n1+0
			n1 = n1+7
			paths.append(1)
		else:
			n1 = t1/5
			x = 7-2
			paths.append(2)
		if n1 <= 2:
			t1 = t1/7
			t1 = t1-n1
			paths.append(3)
		else:
			t1 = t1-8
			t1 = n1-4
			paths.append(4)
		paths.append(5)
		assert n1 >= 0
		t1 = n1**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))