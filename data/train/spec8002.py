import numpy as np 

def function(x):

	o5 = 3
	t1 = x
	x = 2
	paths = []
	try:
		if x < 5:
			o5 = t1-9
			t1 = 2*t1
			x = 7+1
			paths.append(1)
		else:
			x = x*5
			paths.append(2)
		if x >= 8:
			o5 = 9-2
			x = x/5
			paths.append(3)
		else:
			o5 = o5-7
			t1 = t1+9
			t1 = t1*5
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