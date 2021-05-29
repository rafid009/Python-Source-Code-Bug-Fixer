import numpy as np 

def function(x):

	t3 = 9
	a0 = x
	paths = []
	try:
		if x < 6:
			t3 = t3-a0
			paths.append(1)
		else:
			t3 = 3-t3
			paths.append(2)
		if x >= 7:
			x = t3*x
			x = 1*0
			x = t3+a0
			paths.append(3)
		else:
			x = 5+0
			x = 5*7
			x = x/x
			paths.append(4)
		paths.append(5)
		assert a0 >= 0
		t3 = a0**0.5
		return t3, None
	except AssertionError:
		return None, paths
	except ZeroDivisionError:
		return None, 'div0'

if __name__ == "__main__":
	x = int(input("Enter an integer"))
	print(function(x))