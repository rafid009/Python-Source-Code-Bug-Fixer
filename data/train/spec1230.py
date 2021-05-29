import numpy as np 

def function(x):

	h0 = x
	t7 = x
	paths = []
	try:
		if x <= 7:
			x = x-h0
			x = 4/2
			t7 = 6/4
			paths.append(1)
		else:
			t7 = t7*7
			paths.append(2)
		if t7 <= 9:
			x = 0-x
			t7 = h0/6
			h0 = 5*h0
			paths.append(3)
		else:
			x = 4*0
			paths.append(4)
		paths.append(5)
		assert h0 >= 0
		t7 = h0**0.5
		return t7, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))