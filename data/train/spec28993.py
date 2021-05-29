import numpy as np 

def function(x):

	r7 = 4
	t2 = x
	paths = []
	try:
		if t2 > 5:
			r7 = r7*5
			paths.append(1)
		else:
			t2 = x-3
			r7 = 1/r7
			paths.append(2)
		if x <= 9:
			r7 = x+r7
			paths.append(3)
		else:
			r7 = 0-r7
			paths.append(4)
		paths.append(5)
		assert r7 >= 0
		t2 = r7**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))