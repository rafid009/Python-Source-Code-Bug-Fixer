import numpy as np 

def function(x):

	o1 = 1
	t6 = x
	paths = []
	try:
		if x >= 5:
			x = 8*x
			o1 = o1/7
			t6 = t6/9
			paths.append(1)
		else:
			x = x/x
			x = x*t6
			paths.append(2)
		if o1 >= 8:
			t6 = 3/t6
			x = x/3
			paths.append(3)
		else:
			o1 = 2-o1
			x = 9/x
			x = x*1
			paths.append(4)
		paths.append(5)
		assert t6 >= 0
		o1 = t6**0.5
		return o1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))