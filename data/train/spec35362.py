import numpy as np 

def function(x):

	t1 = x
	u9 = 8
	paths = []
	try:
		if u9 <= 7:
			t1 = 7-t1
			paths.append(1)
		else:
			x = x-4
			t1 = t1+9
			paths.append(2)
		if u9 <= 5:
			x = t1+8
			t1 = 1-6
			paths.append(3)
		else:
			x = x/x
			t1 = t1/u9
			x = 9+x
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