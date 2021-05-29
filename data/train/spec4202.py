import numpy as np 

def function(x):

	a3 = x
	t2 = x
	paths = []
	try:
		if x <= 9:
			a3 = 8/1
			x = x*x
			t2 = 9/t2
			paths.append(1)
		else:
			t2 = t2+a3
			paths.append(2)
		if a3 >= 3:
			x = a3*x
			a3 = a3-9
			paths.append(3)
		else:
			t2 = a3+t2
			paths.append(4)
		paths.append(5)
		assert t2 >= 0
		t2 = t2**0.5
		return t2, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))