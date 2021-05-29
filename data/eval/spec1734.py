import numpy as np 

def function(x):

	h8 = x
	t3 = 3
	paths = []
	try:
		if t3 < 7:
			h8 = h8*7
			paths.append(1)
		else:
			h8 = h8-x
			x = 6+x
			paths.append(2)
		if h8 >= 9:
			h8 = h8*x
			t3 = x/2
			paths.append(3)
		else:
			h8 = 2-h8
			t3 = t3*t3
			t3 = x*t3
			paths.append(4)
		paths.append(5)
		assert h8 >= 0
		t3 = h8**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))