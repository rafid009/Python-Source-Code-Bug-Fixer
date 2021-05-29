import numpy as np 

def function(x):

	t1 = 4
	o6 = x
	paths = []
	try:
		if t1 < 1:
			t1 = t1/1
			x = 1+8
			paths.append(1)
		else:
			x = 7-t1
			o6 = o6+9
			o6 = 6+7
			paths.append(2)
		if o6 > 5:
			t1 = x-t1
			x = 7/x
			paths.append(3)
		else:
			t1 = o6-x
			x = t1/x
			x = 6+x
			paths.append(4)
		paths.append(5)
		assert t1 >= 0
		t1 = t1**0.5
		return t1, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))