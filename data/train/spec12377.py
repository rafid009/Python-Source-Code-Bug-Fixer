import numpy as np 

def function(x):

	f1 = x
	t2 = x
	x = x
	paths = []
	try:
		if t2 > 7:
			f1 = 2/5
			t2 = f1+f1
			paths.append(1)
		else:
			f1 = f1*9
			x = 1+x
			paths.append(2)
		if t2 <= 2:
			f1 = f1+4
			paths.append(3)
		else:
			f1 = 7/4
			t2 = 9/8
			x = x+7
			paths.append(4)
		paths.append(5)
		assert x >= 0
		t2 = x**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))