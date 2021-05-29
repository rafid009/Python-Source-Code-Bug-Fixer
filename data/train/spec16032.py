import numpy as np 

def function(x):

	t5 = 3
	h2 = x
	x = x
	paths = []
	try:
		if t5 <= 5:
			t5 = t5/x
			x = 9+h2
			t5 = 6*2
			paths.append(1)
		else:
			h2 = h2*8
			paths.append(2)
		if x < 9:
			t5 = 1+t5
			paths.append(3)
		else:
			h2 = h2-h2
			t5 = h2*3
			paths.append(4)
		paths.append(5)
		assert h2 >= 0
		t5 = h2**0.5
		return t5, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))