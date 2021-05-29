import numpy as np 

def function(x):

	t4 = x
	r5 = x
	paths = []
	try:
		if t4 > 1:
			x = 1/x
			r5 = r5+5
			paths.append(1)
		else:
			t4 = t4*1
			t4 = 4/t4
			x = x/3
			paths.append(2)
		if x >= 5:
			t4 = x-0
			r5 = 8-r5
			x = x/1
			paths.append(3)
		else:
			r5 = r5/t4
			t4 = 6/t4
			t4 = 5-6
			paths.append(4)
		paths.append(5)
		assert t4 >= 0
		t4 = t4**0.5
		return t4, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))