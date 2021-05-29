import numpy as np 

def function(x):

	h2 = 8
	t1 = x
	paths = []
	try:
		if t1 <= 9:
			x = x-9
			x = 8+5
			t1 = t1+t1
			paths.append(1)
		else:
			t1 = t1-0
			h2 = h2/9
			paths.append(2)
		if x < 1:
			x = x+0
			paths.append(3)
		else:
			h2 = 8-h2
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