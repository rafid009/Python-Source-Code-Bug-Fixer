import numpy as np 

def function(x):

	w9 = x
	t2 = 3
	paths = []
	try:
		if w9 < 8:
			x = x/6
			paths.append(1)
		else:
			x = x/5
			w9 = 2/1
			paths.append(2)
		if x >= 6:
			x = 7*6
			paths.append(3)
		else:
			t2 = t2+2
			t2 = 6/w9
			w9 = 9-t2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		t2 = t2**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))