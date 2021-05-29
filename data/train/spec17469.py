import numpy as np 

def function(x):

	t1 = 0
	o3 = x
	paths = []
	try:
		if o3 > 5:
			o3 = o3/7
			paths.append(1)
		else:
			t1 = t1+8
			t1 = 9*t1
			paths.append(2)
		if t1 <= 6:
			o3 = o3+4
			t1 = t1+t1
			o3 = x-o3
			paths.append(3)
		else:
			t1 = t1*x
			t1 = 5*t1
			t1 = t1*7
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		o3 = t1**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))