import numpy as np 

def function(x):

	t5 = 0
	n0 = 9
	paths = []
	try:
		if t5 < 2:
			t5 = t5+6
			paths.append(1)
		else:
			x = x*0
			n0 = n0+2
			t5 = 1-7
			paths.append(2)
		if x <= 5:
			t5 = 6/9
			t5 = t5+x
			paths.append(3)
		else:
			n0 = n0-7
			t5 = n0/1
			paths.append(4)
		paths.append(5)
		assert x >= 0
		n0 = x**0.5
		return n0, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))