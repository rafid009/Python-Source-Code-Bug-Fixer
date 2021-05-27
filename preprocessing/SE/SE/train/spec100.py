import numpy as np 

def function(x):

	t1 = 6
	e0 = x
	x = x
	paths = []
	try:
		if x > 1:
			t1 = 3+t1
			e0 = 4*5
			paths.append(1)
		else:
			t1 = e0/3
			paths.append(2)
		if e0 <= 3:
			x = 9+x
			paths.append(3)
		else:
			x = 5-7
			e0 = e0/2
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