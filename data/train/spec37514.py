import numpy as np 

def function(x):

	t5 = x
	r5 = x
	paths = []
	try:
		if x > 8:
			t5 = 0/r5
			r5 = r5/r5
			paths.append(1)
		else:
			x = 5*x
			r5 = 7-8
			paths.append(2)
		if r5 >= 6:
			t5 = r5+1
			t5 = 4/3
			r5 = r5+1
			paths.append(3)
		else:
			t5 = t5/4
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