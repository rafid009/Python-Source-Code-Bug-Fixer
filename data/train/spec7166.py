import numpy as np 

def function(x):

	w3 = 8
	t1 = 0
	paths = []
	try:
		if x > 5:
			x = w3+x
			x = 6-2
			w3 = w3-t1
			paths.append(1)
		else:
			t1 = t1+7
			x = x/x
			paths.append(2)
		if t1 > 5:
			x = 2*x
			w3 = w3/x
			paths.append(3)
		else:
			t1 = 4-w3
			x = t1-6
			x = t1+7
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