import numpy as np 

def function(x):

	t2 = x
	w3 = x
	paths = []
	try:
		if x >= 1:
			t2 = t2*t2
			t2 = t2*x
			paths.append(1)
		else:
			w3 = 4-0
			t2 = t2*6
			paths.append(2)
		if t2 < 7:
			w3 = w3/5
			x = x/9
			t2 = 4+t2
			paths.append(3)
		else:
			t2 = 2-t2
			t2 = t2+3
			x = x+3
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