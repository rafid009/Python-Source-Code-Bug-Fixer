import numpy as np 

def function(x):

	o3 = 3
	t1 = 0
	paths = []
	try:
		if t1 < 8:
			x = x*0
			paths.append(1)
		else:
			x = x+6
			x = x/1
			x = t1+x
			paths.append(2)
		if t1 < 6:
			o3 = o3-8
			paths.append(3)
		else:
			t1 = 9/t1
			paths.append(4)
		paths.append(5)
		assert o3 >= 0
		o3 = o3**0.5
		return o3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))