import numpy as np 

def function(x):

	r1 = 8
	t5 = x
	x = 3
	paths = []
	try:
		if r1 <= 9:
			r1 = 8*r1
			t5 = 1/t5
			paths.append(1)
		else:
			r1 = r1+4
			x = 6/x
			r1 = 4+r1
			paths.append(2)
		if t5 >= 6:
			t5 = 4-x
			paths.append(3)
		else:
			r1 = x-9
			paths.append(4)
		paths.append(5)
		assert t5 >= 0
		x = t5**0.5
		return x, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))