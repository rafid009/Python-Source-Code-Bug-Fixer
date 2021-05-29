import numpy as np 

def function(x):

	r9 = x
	t3 = x
	paths = []
	try:
		if r9 <= 8:
			x = 0/x
			x = 6*x
			paths.append(1)
		else:
			x = x+2
			r9 = 2*4
			t3 = t3+5
			paths.append(2)
		if t3 < 8:
			x = r9-r9
			t3 = 9+t3
			x = x+3
			paths.append(3)
		else:
			t3 = t3/6
			paths.append(4)
		paths.append(5)
		assert t3 >= 0
		t3 = t3**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))